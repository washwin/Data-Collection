import requests
from bs4 import BeautifulSoup

def fetch_britannica_text():
    # base_url = "https://www.britannica.com/topic/"
    # url = f"{base_url}{article_title}"
    url = "https://www.refseek.com/directory/encyclopedias.html"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
        return None
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
        return None
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
        return None
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract text from paragraphs
    paragraphs = soup.find_all('p')
    text = '\n'.join([paragraph.get_text() for paragraph in paragraphs])

    print(text)

fetch_britannica_text()