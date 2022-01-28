#http://quotes.toscrape.com/ - написати скрейпер для збору всієї доступної інформації про записи:
#цитата, автор, інфа про автора... Отриману інформацію зберегти в CSV файл та в базу. Результати зберегти в репозиторії.
#Пагінацію по сторінкам робити динамічною (знаходите лінку на наступну сторінку і берете з неї URL). 



import os
import requests
from bs4 import BeautifulSoup
import csv
import sqlite3


def write_headers_to_csv(csv_file, csv_columns):
    try:
        with open(csv_file, 'r+', encoding="utf-8") as dump:
            if not dump.read():
                writer = csv.DictWriter(dump, fieldnames=csv_columns)
                writer.writeheader()
    except FileNotFoundError:
        with open(csv_file, 'w', encoding="utf-8") as dump:
            writer = csv.DictWriter(dump, fieldnames=csv_columns)
            writer.writeheader()


def write_dict_to_csv(csv_file, csv_columns, dict_data):
    with open(csv_file, 'a', encoding="utf-8") as dump:
        writer = csv.DictWriter(dump, fieldnames=csv_columns)
        writer.writerow(dict_data)


def authors_db(authors_list):
    if os.path.isfile('author_data.db'):
        os.remove('author_data.db')

    con = sqlite3.connect('author_data.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS author(author_quote TEXT NOT NULL,text_quote TEXT NOT NULL,author_born 
    TEXT NOT NULL,author_born_place TEXT NOT NULL,about_author TEXT NOT NULL)''')

    cur.executemany('''INSERT INTO author VALUES (?, ?, ?, ?, ?)''', authors_list)

    con.commit()
    con.close()


def main():
    next_page_url = ''
    has_next = True

    columns = ["Quote", "Author", "AuthorBornDate", "AuthorBornPlace", "AboutAuthor"]
    write_headers_to_csv("author.csv", columns)

    authors_db_list = []

    while has_next:
        url = "http://quotes.toscrape.com" + next_page_url
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.select('div[class="quote"]')

        for quote in quotes:
            author_text = quote.select_one('span[class="text"]').text.strip().replace('“', '').replace('”', '')
            author = quote.select_one('small[class="author"]').text.strip()

            link = quote.select("span > a")[0].get("href")

            author_response = requests.get('http://quotes.toscrape.com' + link).text
            author_soup = BeautifulSoup(author_response, 'lxml')

            b_day = author_soup.select_one('span[class="author-born-date"]').text.strip()
            location = author_soup.select_one('span[class="author-born-location"]').text.strip()
            author_biograf = author_soup.select_one('div[class="author-description"]').text.strip()

            result_data = {"Quote": author_text, "Author": author, "AuthorBornDate": b_day,
                           "AuthorBornPlace": location,
                           "AboutAuthor": author_biograf}

            authors_db_list.append((author, author_text, b_day, location, author_biograf))

            write_dict_to_csv("author.csv", columns, result_data)

            authors_db(authors_db_list)

        try:
            next_page_url = soup.select('ul.pager')[0].select('li.next a')[0].get('href')
        except:
            has_next = False


main()
