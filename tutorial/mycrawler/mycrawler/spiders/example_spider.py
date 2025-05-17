import scrapy


class ExampleSpiderSpider(scrapy.Spider):
    name = "example_spider"
    allowed_domains = ["youtube.com"]
    start_urls = ["https://youtube.com"]

    def parse(self, response):
        pass
