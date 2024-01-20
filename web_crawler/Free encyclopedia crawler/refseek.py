from bs4 import BeautifulSoup
import requests
import re


def fetch_refseek_text(article_title):
    source = requests.get(f'https://www.refseek.com/search?q={article_title}').text
    main = BeautifulSoup(source, 'lxml')

    all_text = ["ok"]
    http_links = main.find_all('a', href=re.compile(r'^https?://'))
    for link in http_links:
        try:
            response = requests.get(link['href'])
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            print(f"HTTP Error: {errh}")
        except requests.exceptions.ConnectionError as errc:
            print(f"Error Connecting: {errc}")
        except requests.exceptions.Timeout as errt:
            print(f"Timeout Error: {errt}")
        except requests.exceptions.RequestException as err:
            print(f"An unexpected error occurred: {err}")

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from paragraphs
        paragraphs = soup.find_all('p')
        text = [paragraph.get_text(strip=True) for paragraph in paragraphs]
        all_text.append(text)

    return all_text

# print(fetch_refseek_text("India"))
