import scrapy
from ..items import SangaiExpressItem

class NewsSpider(scrapy.Spider):
    def response_is_ban(self, request, response):
        return b'banned' in response.body

    def exception_is_ban(self, request, exception):
        return None
    

    name = "sangai"
    start_urls = [
        "https://epaper.thesangaiexpress.com/index.php?edition=Mpage&date=2024-01-29&page=1"
        ]
    page_number = 1
    def parse(self, response):
        items = SangaiExpressItem()

        # date = response.css('#date_selector::text').extract()
        # product_price = response.css('.a-price-whole::text').extract()
        image = response.css('.s-image::attr(src)').get()

        # items['date'] = date
        # items['product_price'] = product_price
        items['image'] = image
        
        yield items

        next_page = f"https://epaper.thesangaiexpress.com/index.php?edition=Mpage&date=2024-01-29&page={str(NewsSpider.page_number)}"
        if NewsSpider.page_number <= 30:
            NewsSpider.page_number = NewsSpider.page_number + 1
            yield response.follow(next_page, callback = self.parse)