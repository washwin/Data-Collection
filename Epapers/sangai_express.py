# %%
from bs4 import BeautifulSoup
import requests
import csv

# %%
source = requests.get('https://www.thesangaiexpress.com/').text
soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())

# %%
links = soup.find_all("a")
article_links = set()
category_links = set()
for link in links:
    href = link.get("href")
    if href:
        if href.endswith(".html") and href.startswith("https"):
            if href.strip('/').split('/')[-2] == "www.thesangaiexpress.com":
                category_links.add(href)
            else:
                article_links.add(href)

for clink in category_links:
    source = requests.get(clink).text
    soup = BeautifulSoup(source, 'html.parser')
    links = soup.find_all("a", class_="btn btn-red")
    for link in links:
        href = link.get("href")
        article_links.add(href)
        print(href)

# %%
with open('extracted_data/sangaiexpress_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Content'])
    for link in article_links:
        last_slash_index = link.rfind("/")
        title_with_extension = link[last_slash_index + 1:]
        title = title_with_extension.replace(".html", "")
        source1 = requests.get(link).text
        soup1 = BeautifulSoup(source1, 'html.parser')
        text = soup1.find("div", class_="body_container").get_text(strip=True)
        writer.writerow([title, text])
csvfile.close()


