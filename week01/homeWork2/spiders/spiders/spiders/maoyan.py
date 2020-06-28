import scrapy
from scrapy.selector import Selector
from spiders.items import SpidersItem

class MaoyanSpider(scrapy.Spider):

    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        movie_list = Selector(response=response).xpath('//div[@class="movie-item film-channel"]')
        for i in range(10):
            movie = movie_list[i]
            item = SpidersItem()
            item['movie_name'] = movie.xpath('.//span[contains(@class,"name")]/text()').extract_first()
            type_date = movie.xpath('.//span[@class="hover-tag"]/../text()').extract()
            item['movie_type'] = type_date[1].strip('\n').strip()
            item['movie_time'] = type_date[5].strip('\n').strip()
            yield item

