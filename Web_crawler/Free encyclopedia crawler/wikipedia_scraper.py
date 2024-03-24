import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_text(article_title):
    base_url = "https://en.wikipedia.org/wiki/"
    url = f"{base_url}{article_title}"
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
    text = [paragraph.get_text(strip=True) for paragraph in paragraphs]

    return text