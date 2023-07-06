import base64
import requests
import token_renew
import glob

# 请求URL
request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/handwriting"
access_token = "24.e3db66daecd7a02da28ce762d0d449281.282335-31849829"
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}

# 文件目录
# directory = "zuowen/"
# # 找到所有jpg和png文件
# image_files = glob.glob(directory + "*.jpg") + glob.glob(directory + "*.png") + glob.glob(directory + "*.jpeg")
# i=0
# for image_file in image_files:
def get_ocr_text(image_file):
    with open(image_file, 'rb') as f:
        img = base64.b64encode(f.read())
        params = {"image": img}
        response = requests.post(request_url, data=params, headers=headers)

        words_txt = ""
        if response:
            try:
                res = response.json()
                if res.get('error_code') == 110:
                    print('token过期')
                    token_renew.get_token()
                    # return get_ocr_text(image_file)
                print(res)
                # words_result_list = response.json().get("words_result")
                # print(words_result_list)
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

print(get_ocr_text("../zuowen/微信图片_20230623133037.jpg"))