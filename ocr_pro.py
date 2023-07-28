import pytesseract

from PIL import Image

def ocr_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image, lang='chi_sim')
    return text

# text = ocr_image('data\\20230623133051.jpg')
# print(text)




