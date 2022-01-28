# Легенда:
#     - Клієнт для свого проєкта замовив у вас бота, який буде створювати файл з новинами про події у місті за певний день. Клієнт має певні побажання щодо формату файлу, даних у ньому та технологіях, які будуть використовуватися (клієнт планує сам підтримувати свій проєкт, але він знає лише Python та трохи розбирається у Scrapy і BeautifulSoup)
#
# Завдання:
#     Напишіть скрейпер для сайту "vikka.ua", який буде приймати від користувача дату, збирати і зберігати інформацію про новини за вказаний день.
#
# Особливості реалізації:
#     - використовувати лише Scrapy, BeautifulSoup (опціонально), lxml (опціонально) та вбудовані модулі Python
#     - дані повинні зберігатися у csv файл з датою в якості назви у форматі "рік_місяць_число.csv" (напр. 2022_01_13.csv)
#     - дані, які потрібно зберігати (саме в такому порядку вони мають бути у файлі):
#         1. Заголовок новини
#         2. Текст новини у форматі рядка без HTML тегів та у вигляді суцільного тексту (Добре: "Hello world" Погано: "<p>Hello</p><p>world</p>")
#         3. Теги у форматі рядка, де всі теги записані з решіткою через кому (#назва_тегу, #назва_тегу, ...)
#         4. URL новини
#     - збереження даних у файл може відбуватися за бажанням або в самому спайдері, або через Pipelines (буде плюсом в карму)
#     - код повинен бути написаний з дотриманням вимог PEP8 (іменування змінних, функцій, класів, порядок імпортів, відступи, коментарі, документація і т.д.)
#     - клієнт не повинен здогадуватися, що у вас в голові - додайте якісь підказки там, де це необхідно
#     - клієнт може випадково ввести некорректні дані, пам'ятайте про це
#     - якщо клієнту доведеться відправляти вам бота на доопрацювання багато разів, або не всі його вимоги будуть виконані - він знайде іншого виконавця, а з вами договір буде розірваний. У нього в команді немає тестувальників, тому перед відправкою завдання - впевніться, що все працює і відповідає ТЗ.
#     - не забудьте про requirements.txt
#     - клієнт буде запускати бота через термінал командою "scrapy crawl назва_скрейпера"
#


import scrapy

from datetime import datetime
from bs4 import BeautifulSoup

from ..items import Task1Item


class NewsvikkascraperSpider(scrapy.Spider):
    """ Class to scrape information from a website"""
    name = 'newsvikkascraper'
    allowed_domains = ['vikka.ua']
    start_urls = ['https://www.vikka.ua/category/novini/']

    def __init__(self, name=None):
        super().__init__(name)
        self.data_user = None

    def check_date(self):
        """Metod to check user input data"""
        user_data = input("Input your data yyyy.mm.dd: ")

        try:
            check_user_date = datetime.strptime(user_data, "%Y.%m.%d")
            data_today = datetime.today().strftime('%Y.%m.%d')
            current_data = datetime.strptime(data_today, "%Y.%m.%d")
            if check_user_date > current_data:
                print("Please enter the correct date!")
            else:
                return user_data.split('.')
        except ValueError:
            print('The date {} is invalid'.format(user_data))

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
        soup = BeautifulSoup(news.text, "lxml")
        tags = ''
        for tag in soup.select('.post-tag'):
            if not tags:
                tags += '#' + tag.text
            else:
                tags += ', #' + tag.text
        title = soup.select_one('h1.post-title').text.strip()
        text = soup.select_one('.entry-content.-margin-b').text.strip()
        tags = tags
        url = news.url
        yield Task1Item(title=title, text=text, tags=tags, url=url)
