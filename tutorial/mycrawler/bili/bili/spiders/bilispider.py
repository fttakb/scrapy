import scrapy

class BilispiderSpider(scrapy.Spider):
    name = "bilispider"
    allowed_domains = ["search.bilibili.com"]
    start_urls = ["https://search.bilibili.com/all?keyword=猴子&page=1"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers={
                    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36"
                },
                callback=self.parse,
            )

    def parse(self, response):
        for item in response.css("div.bili-video-card__info--right"):
            yield {
                "title": item.css("h3::text").get(),
                "url": item.css("a::attr(href)").get(),
            }

        # 抓“下一页”按钮链接
        next_page = response.css("li.pagination-next a::attr(href)").get()
        if next_page:
            yield scrapy.Request(
                url=response.urljoin(next_page),
                headers={"User-Agent": "Mozilla/5.0 (...)"},
                callback=self.parse
            )