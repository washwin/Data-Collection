import scrapy


class HypSpider(scrapy.Spider):
    name = "hyp"
    # allowed_domains = ["x"]
    start_urls = ["https://hueiyenlanpao.com/"]

    # def parse(self, response):
    #     for book in response.css('.col'):
    #         title = book.css('h5 ::text').get()
    #         link = response.urljoin(
    #             book.css('a.pdf ::attr(href)').get()
    #         )
    #         yield {
    #             'Title':title,
    #             'file_urls':[link]
    #         }

    def parse(self, response):
        # Extract HTML source code
        html_source = response.body
        # You can do something with the HTML source, like save it to a file
        with open('page.html', 'wb') as f:
            f.write(html_source)
