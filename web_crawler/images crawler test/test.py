import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_images(url, download_folder):
    os.makedirs(download_folder, exist_ok=True)
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all image tags
        img_tags = soup.find_all('img')
        
        for img_tag in img_tags:
            # Get the source URL of the image
            img_url = img_tag.get('src')
            
            # Handle relative URLs by joining them with the base URL
            img_url = urljoin(url, img_url)
            
            # Send a GET request to the image URL
            img_response = requests.get(img_url)
            
            # Check if the request was successful
            if img_response.status_code == 200:
                # Extract the image file name
                img_name = os.path.basename(img_url)
                
                # Create the file path for the downloaded image
                img_path = os.path.join(download_folder, img_name)
                
                # Save the image to the file path
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_response.content)
                
                print(f"Downloaded: {img_path}")
            else:
                print(f"Failed to download image from {img_url}")

    else:
        print(f"Failed to fetch URL: {url}")

if __name__ == "__main__":
    website_url = "https://epaper.thesangaiexpress.com/index.php?edition=Mpage&date=2024-01-13&page=1"  # Replace with the URL of the website
    download_folder = "downloaded_images"  # Choose a folder to save the images
    
    download_images(website_url, download_folder)
