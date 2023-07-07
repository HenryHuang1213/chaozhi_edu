import json
import os
import random

import streamlit as st
from PIL import Image

from parse_csv import Parse_CSV
from web_api import Teacher
from OCR_pkg import baidu_ocr


def pic_eval(title, content):
    evaluation = Teacher.get_article_eval('', title, 0, content)
    st.session_state['article_type'] = 'article'
    # print(evaluation)
    st.session_state['evaluation'] = json.loads(evaluation)


def show():
    st.title("上传作文")
    if 'lrbutton_clicked' not in st.session_state:
        st.session_state['lrbutton_clicked'] = False
    if 'ocr_history' not in st.session_state:
        st.session_state['ocr_history'] = ''

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

            col1, col2, col3 = st.columns(3)

            if col1.button('向左旋转90度'):
                image = image.rotate(90, expand=True)
                image.save('zuowen/temp.jpg')

            if col2.button('向右旋转90度'):
                image = image.rotate(-90, expand=True)
                image.save('zuowen/temp.jpg')

            if col3.button('确认'):
                # image.save('zuowen/temp.jpg')

                st.session_state['lrbutton_clicked'] = True
                st.experimental_rerun()

            st.image(image, caption='所上传的图片', use_column_width=True)
        else:

            if st.session_state['ocr_history'] == '':
                dir_path = os.path.dirname(os.path.realpath(__file__))
                pic_file_path = os.path.join(dir_path, 'zuowen/temp.jpg')
                res_raw = baidu_ocr.get_pic_text(pic_file_path)
                st.session_state['ocr_history'] = res_raw
            res = json.loads(st.session_state['ocr_history'])
            title = res['文章题目']
            content = res['文章正文']
            st.write('识别文字结果为：')
            st.markdown(f"*文章题目:*  《{title}》")
            st.markdown(f"*文章正文:*  \n\n {content}")

            if st.button('确认结果并进行批改'):
                st.write("正在批改...")
                pic_eval(title, content)
                st.session_state['history'] = ['', title, 0, content]
                st.session_state['page'] = 'eval'
                st.session_state['marking'] = 'submitted'
                st.experimental_rerun()
