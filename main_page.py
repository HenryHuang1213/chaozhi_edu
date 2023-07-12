import streamlit as st
import os
import random


def start_mark():
    st.session_state['marking'] = 'working'
    st.session_state['history'] = []
    st.session_state['evaluation'] = []
    st.session_state['article_type'] = ''


def show():
    if 'marking' not in st.session_state:
        st.session_state['marking'] = ''
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    if 'evaluation' not in st.session_state:
        st.session_state['evaluation'] = []
    if 'article_type' not in st.session_state:
        st.session_state['article_type'] = ''
    if 'random_id' not in st.session_state:
        random_number = random.randint(10000000, 99999999)
        while os.path.exists(f'zuowen/{random_number}.jpg'):
            random_number = random.randint(10000000, 99999999)
        st.session_state['random_id'] = random_number
    if 'Evaluation_Cost_Time' not in st.session_state:
        st.session_state['Evaluation_Cost_Time'] = 0

    if st.button("开始新的批改"):
        st.session_state['page'] = 'eval'
        start_mark()
        st.experimental_rerun()
    if st.session_state['marking'] == 'submitted':
        if st.button("查看刚才的批改"):
            st.session_state['page'] = 'eval'
            st.experimental_rerun()
    if st.button("查看作文库"):
        st.session_state['page'] = 'library'
        st.experimental_rerun()
    if st.button("上传作文图片"):
        st.session_state['page'] = 'newpic'
        st.experimental_rerun()
