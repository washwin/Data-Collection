import urllib.request 
from PIL import Image 

# Retrieving the resource located at the URL 
# and storing it in the file name a.png 
url = "https://epaperlokmat.in/eNewspaper/News/LOK/MULK/2024/01/10/ArticleImages/659db0b4e0fe7.jpg" 
urllib.request.urlretrieve(url, "test_image.png") 

# # Opening the image and displaying it (to confirm its presence) 
# img = Image.open(r"test_image.png") 
# img.show()
