from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

im = Image.open('languages/hin2.png')
lang = "hin"

tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'
text = pytesseract.image_to_string(im, lang=lang, config=tessdata_dir_config)
print(text)