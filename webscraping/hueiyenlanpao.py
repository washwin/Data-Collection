import requests
from datetime import timedelta, date

def download_pdf(url, name, directory):
    save_path = f"downloaded_pdfs/{directory}/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as pdf_file:
            pdf_file.write(response.content)
        print(f"PDF downloaded successfully and saved at: {save_path}")
    else:
        print(f"Failed to download PDF. Status code: {response.status_code}")

def check_link_existence(url):
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200
    except requests.ConnectionError:
        return False
    
def fetch_hueiyenlanpao():
    start_date = date(2024, 1, 1)   #year, month, day
    end_date = date(2024, 3, 1)
    day = 1
    month = 1
    year = 2024
    dates = []
    current_date = start_date
    while current_date <= end_date:
        dates.append(current_date)
        current_date += timedelta(days=1)

    links = []
    directory = "hueiyenlanpao"
    for d in dates:
        i = 1
        if d.day <10:
            day = f"0{d.day}"
        if d.month < 10:
            month = f"0{d.month}"
        while (True):
            link = f"https://hueiyenlanpao.com/wp-content/uploads/2016/06/{day}.{month}.{d.year}-B{i}.pdf"
            i = i + 1
            if check_link_existence(link):
                links.append(link)
                print(link)
                name = f"{d.year}-{month}-{day}:{i}.pdf"
                download_pdf(link, name, directory)
            else:
                break

fetch_hueiyenlanpao()