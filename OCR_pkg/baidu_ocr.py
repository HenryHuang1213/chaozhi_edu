import base64
import requests
from .ocr_config import OCR_Config
from .optimize_text import get_completion
import glob


# 文件目录
# directory = "zuowen/"
# # 找到所有jpg和png文件
# image_files = glob.glob(directory + "*.jpg") + glob.glob(directory + "*.png") + glob.glob(directory + "*.jpeg")
# i=0
# for image_file in image_files:
def get_ocr_text_from_file(image_file):
    ocr_c = OCR_Config()
    request_url, headers = ocr_c.get_req_config()
    with open(image_file, 'rb') as f:
        img = base64.b64encode(f.read())
        params = {"image": img}
        response = requests.post(request_url, data=params, headers=headers)
        words_txt = ""
        if response:
            try:
                res = response.json()
                # print(res)
                while res.get('error_code') == 110:
                    ocr_c.renew_config()
                    request_url, headers = ocr_c.get_req_config()
                    res = requests.post(request_url, data=params, headers=headers).json()
                words_result_list = response.json().get("words_result")
            except:
                words_result_list = []
                print(f"There is an error when OCR the image: {image_file}")
            # if words_result_list is not None:
            for words in words_result_list:
                words_txt += words.get("words") + "\n"
        return words_txt

        # 保存为txt文件
        # txt_file_name = os.path.splitext(os.path.basename(image_file))[0] + ".txt"
        # with open(directory + txt_file_name, 'w') as text_file:
        #     text_file.write(words_txt)


def get_ocr_text_from_image(image):
    ocr_c = OCR_Config()
    request_url, headers = ocr_c.get_req_config()
    img = base64.b64encode(image)
    params = {"image": img}
    response = requests.post(request_url, data=params, headers=headers)

    words_txt = ""
    if response:
        try:
            res = response.json()
            while res.get('error_code') == 110:
                ocr_c.renew_config()
                request_url, headers = ocr_c.get_req_config()
                res = requests.post(request_url, data=params, headers=headers).json()
            words_result_list = response.json().get("words_result")
        except:
            words_result_list = []
            print("There is an error when OCR this image.")
        # if words_result_list is not None:
        for words in words_result_list:
            words_txt += words.get("words") + "\n"

    return words_txt


def get_pic_text(pic_file, pic_type='file'):
    if pic_type == 'file':
        raw_text_word = get_ocr_text_from_file(pic_file)
    else:
        raw_text_word = get_ocr_text_from_image(pic_file)
    return get_completion(raw_text_word)

# text = get_pic_text("../zuowen/temp.jpg")
# print(text)


# text_word = get_ocr_text("../zuowen/微信图片_20230623133037.jpg")
# print(text_word)
# print('-----------------*-----------------')
# artcle = optimize_text.get_completion(text_word)
# print(artcle)
