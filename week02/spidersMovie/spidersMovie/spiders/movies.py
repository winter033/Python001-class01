import scrapy
from bs4 import BeautifulSoup

from spidersMovie.items import SpidersmovieItem
from scrapy.selector import Selector

class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        for i in range(0, 1):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}';
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        print(len(movies))
        for movie in movies:
            movie_name = movie.xpath('./div/span[contains(@class,"name")]/text()').extract_first().strip()
            movie_type_list = movie.xpath('./div/span[@class="hover-tag"]/../text()')
            movie_type = movie_type_list[1].extract().strip()
            movie_time = movie_type_list[5].extract().strip()
            # extract 打印所有数据 ，extract_first 打印第一个 strip去前后空格
            # print(title.extract_first())
            item = SpidersmovieItem()
            item['movie_name'] = movie_name
            item['movie_type'] = movie_type
            item['movie_time'] = movie_time
            yield item


