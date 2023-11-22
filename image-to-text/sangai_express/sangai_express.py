import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

file = open("sangai_express\Text1.txt","w")
img = Image.open('sangai_express\Image1.png')
text = tess.image_to_string(img)
file.write(text)
file.close()

file = open("sangai_express\Text2.txt","w")
img = Image.open('sangai_express\Image2.png')
text = tess.image_to_string(img)
file.write(text)
file.close()

file = open("sangai_express\Text3.txt","w")
img = Image.open('sangai_express\Image3.png')
text = tess.image_to_string(img)
file.write(text)
file.close()

