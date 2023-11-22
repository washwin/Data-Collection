from flask import Flask, render_template, request
from PIL import Image
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tessdata_dir_config = '--tessdata-dir "C:/Program Files/Tesseract-OCR/tessdata"'

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        lang = request.form['language']
        # print(lang)
        temp_image_path = 'temporary_images/temp_image.png'
        image_file.save(temp_image_path)
        extracted_text = perform_ocr(temp_image_path,lang)
        return render_template('index.html', extracted_text=extracted_text)
    return render_template('upload.html')

def perform_ocr(image_path, lang):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("temporary_images/index_gray.png", gray)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    cv2.imwrite("temporary_images/index_blur.png", blur)
    thresh = cv2.threshold(blur, 0, 160, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    cv2.imwrite("temporary_images/index_thresh.png", thresh)
    kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))
    cv2.imwrite("temporary_images/index_kernal.png", kernal)
    dilate = cv2.dilate(thresh, kernal, iterations=1)
    cv2.imwrite("temporary_images/index_dilate.png", dilate)
    cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])
    text = []
    for c in cnts:
        x, y, w, h = cv2.boundingRect(c)
        if h > 200 and w > 20:
            roi = image[y:y+h, x:x+h]
            ocr_result = pytesseract.image_to_string(roi, lang=lang, config=tessdata_dir_config)
            text.append(ocr_result)
            cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2)
    cv2.imwrite("temporary_images/index_bbox_new.png", image)
    return text


if __name__ == '__main__':
    app.run(debug=True)