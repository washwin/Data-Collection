from bs4 import BeautifulSoup
import requests
import re
import os

def download_pdf(url, name, directory):
    save_path = f"downloaded_pdfs/{directory}/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Create directory if not exist
        with open(save_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF downloaded successfully and saved at: {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

def fetch_paochelsalaitaret():
    directory = "paochelsalaitaret"
    source = requests.get('http://paochelsalaitaret.net/ebook.php').text
    main = BeautifulSoup(source, 'lxml')
    http_links = main.find_all('a', href=re.compile(r'\.pdf$'))

    for link in http_links:
        url = f"http://paochelsalaitaret.net/{link.get('href')}"
        name = re.search(r'[^/]+\.pdf$', url).group(0)  # Extract filename from URL using regex
        print(url)
        print(name)
        download_pdf(url, name, directory)

fetch_paochelsalaitaret()
