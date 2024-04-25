# %%
from bs4 import BeautifulSoup
import requests
import csv

# %%
source = requests.get('https://thefrontiermanipur.com/').text
soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())

# %%
category_links_set = set()
author_links_set = set()
feed_links_set = set()
article_links_set = set()
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    if href:
        if href.strip('/').split('/')[-2] == "category":
            category_links_set.add(href)
            # print(href)
        elif href.strip('/').split('/')[-2] == "author":
            author_links_set.add(href)
            # print(href)
        elif href.strip('/').split('/')[-2] == "feed":
            feed_links_set.add(href)
            # print(href)
        elif href.strip('/').split('/')[-3] == "thefrontiermanipur.com":
            article_links_set.add(href)
            # print(href)
    print(href)

for clink in category_links_set:
    source = requests.get(clink).text
    soup = BeautifulSoup(source, 'html.parser')
    links = soup.find_all("a", class_="post-url post-title")
    for link in links:
        href = link.get("href")
        article_links_set.add(href)
        # print(href)
        
for clink in author_links_set:
    source = requests.get(clink).text
    soup = BeautifulSoup(source, 'html.parser')
    links = soup.find_all("a", class_="post-url post-title")
    for link in links:
        href = link.get("href")
        article_links_set.add(href)

for clink in feed_links_set:
    source = requests.get(clink).text
    soup = BeautifulSoup(source, 'html.parser')
    links = soup.find_all("a", class_="post-url post-title")
    for link in links:
        href = link.get("href")
        article_links_set.add(href)

# %%
with open('extracted_data/frontiermanipur_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Content'])
    for link in article_links_set:
        title = link.strip('/').split('/')[-1]
        source1 = requests.get(link).text
        soup1 = BeautifulSoup(source1, 'html.parser')
        text = soup1.find("div", class_="entry-content clearfix single-post-content").get_text(strip=True)
        writer.writerow([title, text])
csvfile.close()


