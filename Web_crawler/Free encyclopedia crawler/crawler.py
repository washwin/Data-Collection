import csv
from wikipedia_scraper import fetch_wikipedia_text
from britannica_scraper import fetch_britannica_text
from refseek import fetch_refseek_text

article_titles = ["Manipur", "Manipur violence"]
for article_title in article_titles:
    wiki_text = fetch_wikipedia_text(article_title)
    if wiki_text:
        csv_file_path = f"data/{article_title}.csv"
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Paragraphs'])
            csv_writer.writerows([[text] for text in wiki_text])
        print(f"Successfully fetched text for {article_title} from Wikipedia")
    else:
        print(f"Failed to fetch text for {article_title} from Wikipedia")

    brita_text = fetch_britannica_text(article_title)
    if brita_text:
        csv_file_path = f"data/{article_title}.csv"
        with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Paragraphs'])
            csv_writer.writerows([[text] for text in brita_text])
        print(f"Successfully fetched text for {article_title} from Britannica")
    else:
        print(f"Failed to fetch text for {article_title} from Britannica")

    refseek_text = fetch_refseek_text(article_title)
    csv_file_path = f"data/{article_title}.csv"
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Paragraphs'])
        csv_writer.writerows([[text] for text in refseek_text])