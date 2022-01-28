#Переробити попереднє домашнє завдання: зберігати результати в базу, використовуючи pipelines.
import scrapy

from datetime import datetime
from bs4 import BeautifulSoup

from ..items import Task1Item


class NewsvikkascraperSpider(scrapy.Spider):
    name = 'newsvikkascraper'
    allowed_domains = ['vikka.ua']
    start_urls = ['https://www.vikka.ua/category/novini/']

    def check_date(self):
        """Metod to check user input data"""
        try:
            self.user_data = input("Input your data yyyy.mm.dd: ")
            check_user_date = datetime.strptime(self.user_data, "%Y.%m.%d")
            data_today = datetime.today().strftime('%Y.%m.%d')
            current_data = datetime.strptime(data_today, "%Y.%m.%d")
            if check_user_date > current_data:
                print("Please enter the correct date!")
            else:
                return self.user_data.split('.')
        except ValueError:
            print('The date {} is invalid'.format(self.user_data))

    def start_requests(self):
        """Metod to start requests"""
        try:
            self.data_user = self.check_date()
            url = f'http://vikka.ua/{self.data_user[0]}/{self.data_user[1]}/{self.data_user[2]}/'
            yield scrapy.Request(
                url=url,
                callback=self.parse_vikkanews_page
            )
        except TypeError:
            print('The date is invalid!')

    def parse_vikkanews_page(self, response):
        """Metod performs site parsing and pagination by pages, if there are several."""
        soup = BeautifulSoup(response.text, "lxml")
        for vikka_news in soup.select('.title-cat-post a'):
            urls = vikka_news.get('href')
            yield scrapy.Request(
                url=urls,
                callback=self.n_parse,
            )

        next_page = soup.select_one('.nav-links a.next.page-numbers')
        if not next_page:
            print('No next page!')
            return
        yield scrapy.Request(
            url=next_page.get('href'),
            callback=self.parse_vikkanews_page
        )

    def n_parse(self, news):
        """Metod collects data from the page"""
        items = Task1Item()
        soup = BeautifulSoup(news.text, "lxml")
        tags = ''
        for tag in soup.select('.post-tag'):
            if not tags:
                tags += '#' + tag.text
            else:
                tags += ', #' + tag.text
        items['data_news'] = self.user_data
        items['title'] = soup.select_one('h1.post-title').text.strip()
        items['text'] = soup.select_one('.entry-content.-margin-b').text.strip()
        items['tags'] = tags
        items['url'] = news.url
        yield items
