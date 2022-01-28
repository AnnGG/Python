# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import csv
import pathlib
import os
from scrapy.exporters import CsvItemExporter
from itemadapter import ItemAdapter

class Task1Pipeline:

    def open_spider(self, spider):
        self.file = open('temp.csv', 'ab')
        self.exporter = CsvItemExporter(self.file, 'UTF-8')
        self.exporter.fields_to_export = ['title', 'text', 'tags', 'url']
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        csv_name = spider.data_user
        try:
            if os.path.exists(f'{csv_name[0]}_{csv_name[1]}_{csv_name[2]}.csv'):
                    os.remove(f'{csv_name[0]}_{csv_name[1]}_{csv_name[2]}.csv')
            os.rename('temp.csv', f'{csv_name[0]}_{csv_name[1]}_{csv_name[2]}.csv')
        except TypeError:
            os.remove('temp.csv')
            print('The date is invalid!')
