# Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
#
# Документація на АПІ:
# https://github.com/HackerNews/API
#
# Скрипт повинен отримувати із командного рядка одну із наступних категорій:
# askstories, showstories, newstories, jobstories
#
# Якщо жодної категорії не указано - використовувати newstories.
# Якщо категорія не входить в список - вивести попередження про це і завершити роботу.
#
# Результати роботи зберегти в CSV файл. Зберігати всі доступні поля. Зверніть увагу - інстанси різних типів мають різний набір полів.
#
# Код повинен притримуватися стандарту pep8.
# Перевірити свій код можна з допомогою ресурсу http://pep8online.com/
#
# Для тих, кому хочеться зробити щось "додаткове" - можете зробити наступне: другим параметром cкрипт може приймати
# назву HTML тега і за допомогою регулярного виразу видаляти цей тег разом із усим його вмістом із значення атрибута "text"
# (якщо він існує) отриманого запису.


import csv
import requests
import sys

from tqdm import tqdm


class HackerNews(object):

    def __init__(self):

        self.categories = ['askstories', 'showstories', 'newstories', 'jobstories']

    def create_url(self, user_input):

        if user_input == '':
            return f'https://hacker-news.firebaseio.com/v0/{self.categories[2]}.json'

        elif user_input in self.categories:
            return f'https://hacker-news.firebaseio.com/v0/{user_input}.json'

        else:
            print("No such category!")
            exit()

    def create_csv(self, u_input):

        article_dicts_list = []
        article_filds = []

        categ_url = self.create_url(u_input)
        category_articles = requests.get(url=categ_url).json()

        for article in tqdm(category_articles):
            article_on_id = f'https://hacker-news.firebaseio.com/v0/item/{article}.json'
            req_article_dict = requests.get(url=article_on_id).json()
            article_dicts_list.append(req_article_dict)
            for key in req_article_dict.keys():
                if key not in article_filds:
                    article_filds.append(key)

        with open('hacker_news.csv', 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=article_filds, restval='None')
            writer.writeheader()
            writer.writerows(article_dicts_list)

if len(sys.argv) == 1:
    cmd_input = ''
else:
    cmd_input = sys.argv[1]

h = HackerNews()
h.create_csv(cmd_input)