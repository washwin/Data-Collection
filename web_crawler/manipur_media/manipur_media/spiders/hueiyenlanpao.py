import scrapy
import requests
from datetime import timedelta, date

class YourSpiderNameSpider(scrapy.Spider):
    name = 'hueiyenlanpao'
    allowed_domains = ['hueiyenlanpao.com']
    start_urls = ['https://hueiyenlanpao.com/wp-content/uploads/2016/06/05.02.2024-B1.pdf']

    def parse(self, response):
        # Extract PDF links from the page
        pdf_links = response.css('a[href$=".pdf"]::attr(href)').extract()
        generated_links = fetch_hueiyenlanpao_links()
        pdf_links.append(generated_links)
        # Download each PDF
        for pdf_link in pdf_links:
            yield scrapy.Request(pdf_link, callback=self.save_pdf)

    def save_pdf(self, response):
        # Save the PDF to a file
        filename = response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')


def fetch_hueiyenlanpao_links():
    start_date = date(2024, 2, 3)
    end_date = date(2024, 2, 4)
    day = 1
    month = 1
    # year = 2024
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)
    links = []
    for d in dates:
        i = 1
        if d.day <10:
            day = f"0{d.day}"
        if d.month < 10:
            month = f"0{d.month}"
        while (True):
            link = f"https://hueiyenlanpao.com/wp-content/uploads/2016/06/{day}.{month}.{d.year}-B{i}.pdf"
            i = i + 1
            links.append(link)
            if check_link_existence(link):
                links.append(link)
            else:
                break
    return links

def check_link_existence(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False