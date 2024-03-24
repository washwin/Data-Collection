import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    # allowed_domains = ["x"]
    start_urls = ["https://en.wikipedia.org/wiki/India"]

    def parse(self, response):
        raw_image_urls = response.css('.mw-file-element').getall()
        clean_image_urls = []
        for img_url in raw_image_urls:
            clean_image_urls.append(response.urljoin(img_url))

        yield{'image_urls' : clean_image_urls}