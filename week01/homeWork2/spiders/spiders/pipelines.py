# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv

class SpidersPipeline:

    def __init__(self):
        self.file = open('movie.csv', 'a+', encoding='utf8', newline='')
        self.writer = csv.writer(self.file, dialect='excel')

    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        self.writer.writerow([movie_name, movie_type, movie_time])
        return item
