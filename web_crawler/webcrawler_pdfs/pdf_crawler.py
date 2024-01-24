from bs4 import BeautifulSoup
import requests
import re

def fetch_links():
    source = requests.get('http://paochelsalaitaret.net/ebook.php').text
    main = BeautifulSoup(source, 'lxml')
    http_links = main.find_all('a', href=re.compile(r'\.pdf$'))

    for link in http_links:
        url = f"http://paochelsalaitaret.net/ebook/{link.get('href')}"
        name = link.get('href').split('/')
        download_pdf(url, name[1])

def download_pdf(url, name):
    save_path = f"downloaded_pdfs/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF downloaded successfully and saved at: {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

fetch_links()