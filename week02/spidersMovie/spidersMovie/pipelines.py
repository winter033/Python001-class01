# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


class SpidersmoviePipeline:
    def __init__(self):
        self.connect = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='admin',
            db='spider'
        )
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        movie_name = item['movie_name']
        movie_type = item['movie_type']
        movie_time = item['movie_time']
        try:
            self.cursor.execute("insert into movie(movie_name,movie_type,movie_time)value (%s,%s,%s)",
                                (movie_name, movie_type, movie_time))
            self.connect.commit()
        except:
            self.rollbask()

        self.close()

        return item
