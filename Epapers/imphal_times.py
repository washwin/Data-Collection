# %%
from bs4 import BeautifulSoup
import requests
import csv

# %%
source = requests.get('https://www.imphaltimes.com/category/articles/').text
soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())

# %%
h2_tags = soup.find_all('h2', class_='penci-entry-title entry-title grid-title')
links = []
for h2_tag in h2_tags:
    a_tag = h2_tag.find('a')
    link = a_tag['href']
    print(link)
    links.append(link)

# %%
with open('extracted_data/imphaltimes_articles.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Content'])
    for link in links:
        title = link.strip('/').split('/')[-1]
        source1 = requests.get(link).text
        soup1 = BeautifulSoup(source1, 'html.parser')
        div_tag = soup1.find('div', id='pryc-wp-acctp-original-content')
        if div_tag:
            p_tags = div_tag.find_all('p')
            content = ""
            for p_tag in p_tags:
                content += p_tag.get_text(strip=True) + " "
            writer.writerow([title, content])  # Write title and content in the same row
        else:
            writer.writerow([title, "No div tag found with the specified id."])  # Write title and error message
csvfile.close()



