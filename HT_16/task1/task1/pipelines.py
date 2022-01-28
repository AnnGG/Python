# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import sqlite3
import os.path

class Task1Pipeline:

    def __init__(self):
        self.conn = sqlite3.connect("news.db")
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS news(
        id integer PRIMARY KEY AUTOINCREMENT,
        data_news TEXT,
        title TEXT,
        body TEXT,
        tags TEXT,       
        url TEXT,
        UNIQUE(url))""")



    def process_item(self, item, spider):

        self.curr.execute("""INSERT OR IGNORE INTO news (data_news, title, body, tags, url) VALUES (?,?,?,?,?)""", (item['data_news'], item['title'], item['text'], item['tags'], item['url']))
        self.conn.commit()
        return item

