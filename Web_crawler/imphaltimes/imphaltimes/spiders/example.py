import scrapy

class ExampleSpider(scrapy.Spider):
    name = "imphal"
    allowed_domains = ["imphaltimes.com"]
    start_urls = ["https://www.imphaltimes.com/category/"]


    def parse(self, response):
        links = response.css('penci-entry-title entry-title grid-title')
        for link in links:
            yield{
                # 'name' : link.css('a::text').get(),
                'url' : link.css('a').attrib['href']
            }
