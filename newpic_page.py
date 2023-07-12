import json
import os

import streamlit as st
from PIL import Image

from web_api import Teacher
from OCR_pkg import baidu_ocr
import time


def pic_eval(title, content):
    evaluation = Teacher.get_article_eval('', title, 0, content)
    st.session_state['article_type'] = 'article'
    # print(evaluation)
    st.session_state['evaluation'] = json.loads(evaluation)

# def get_text_from_pic(pic_file_path):
#     res = baidu_ocr.get_pic_text(pic_file_path)
#     return res

def show():
    st.title("上传作文")
    if 'lrbutton_clicked' not in st.session_state:
        st.session_state['lrbutton_clicked'] = False
    if 'ocr_history' not in st.session_state:
        st.session_state['ocr_history'] = ''
    if 'oriented' not in st.session_state:
        st.session_state['oriented'] = 0

    if st.session_state['marking'] == 'submitted':
        if st.button("查看刚才的批改"):
            st.session_state['page'] = 'eval'
            st.experimental_rerun()
    else:
        if st.button("开始新的批改"):
            st.session_state['page'] = 'eval'
            st.experimental_rerun()
    if st.button("回到主页"):
        st.session_state['page'] = 'main_page'
        st.experimental_rerun()
    if st.button("查看作文库"):
        st.session_state['page'] = 'library'
        st.experimental_rerun()

    uploaded_file = st.file_uploader("请选择需要上传的图片（图片大小不能超过5MB）", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is None:
        st.session_state['lrbutton_clicked'] = False

    if uploaded_file is not None:
        # file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type,
        #                 "FileSize": uploaded_file.size}

        st.write(f"图片已成功上传")

        image = Image.open(uploaded_file)

        # check file size
        if uploaded_file.size > 1000000:  # limit file size under 5MB
            # need compress
            st.write(f"图片需进行压缩")
            image.thumbnail((1000, 1000))

        if not st.session_state['lrbutton_clicked']:
            st.write('请确认图片是否正向')

            col1, col2, col3, col4, col5 = st.columns(5)

            if col1.button('左转'):
                image = image.rotate(90, expand=True)
                image.save(f"zuowen/{st.session_state['random_id']}.jpg")
                st.session_state['oriented'] = 90

            if col2.button('回正'):
                image = image.rotate(0, expand=True)
                image.save(f"zuowen/{st.session_state['random_id']}.jpg")
                st.session_state['oriented'] = 0

            if col3.button('右转'):
                image = image.rotate(-90, expand=True)
                image.save(f"zuowen/{st.session_state['random_id']}.jpg")
                st.session_state['oriented'] = -90

            if col4.button('倒转'):
                image = image.rotate(180, expand=True)
                image.save(f"zuowen/{st.session_state['random_id']}.jpg")
                st.session_state['oriented'] = 180

            if col5.button('确认'):
                image = image.rotate(st.session_state['oriented'], expand=True)
                image.save(f"zuowen/{st.session_state['random_id']}.jpg")
                st.session_state['lrbutton_clicked'] = True
                st.experimental_rerun()

            st.image(image, caption='所上传的图片', use_column_width=True)
        else:
            start_time = time.time()
            # print("PAGE: start time = ", start_time)
            if st.session_state['ocr_history'] == '':
                dir_path = os.path.dirname(os.path.realpath(__file__))
                pic_file_path = os.path.join(dir_path, f"zuowen/{st.session_state['random_id']}.jpg")

                start_time = time.time()
                st.session_state['ocr_history'] = baidu_ocr.get_pic_text(pic_file_path)
                # ocr_result = st.cache_data("ocr_result")

                end_time = time.time()
                st.write(f'OCR GPT Cost Time: {end_time - start_time}s')
            # if ocr_result is None or pic_file_path not in ocr_result:
                # 如果没有缓存，那么计算OCR结果并保存到缓存
                # ocr_result = {pic_file_path: get_text_from_pic(pic_file_path)}
                # st.cache_data("ocr_result", ocr_result)

            res_raw = st.session_state['ocr_history']

            # res_raw = get_text_from_pic(pic_file_path)
                # st.session_state['ocr_history'] = res_raw

            try:
                res = json.loads(res_raw)
            except:
                res = {'文章题目': '', '文章正文': ''}
            end_time = time.time()
            # print("PAGE: end process time = ", end_time)
            # print(f'Total Cost Time: {end_time - start_time}s')
            st.write(f'Total Cost Time: {end_time - start_time}s')
            title = res['文章题目']
            content = res['文章正文']
            st.write('识别文字结果为：')
            if title != '':
                st.markdown(f"*文章题目:*  《{title}》")
            if content != '':
                st.markdown(f"*文章正文:*  \n\n {content}")
            else:
                st.markdown("文章正文未能正确识别，请重新上传图片。上传后请注意调整至正确方位")

            if st.button('确认结果并进行批改'):
                st.write("正在批改...")
                pic_eval(title, content)
                st.session_state['history'] = ['', title, 0, content]
                st.session_state['page'] = 'eval'
                st.session_state['marking'] = 'submitted'
                st.session_state['ocr_history'] = ''
                st.experimental_rerun()
