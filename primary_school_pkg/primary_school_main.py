import streamlit as st
import os
import random

def start_primary_mark():
    st.session_state['primary_marking'] = 'working'
    st.session_state['primary_history'] = []
    st.session_state['primary_evaluation'] = []
    st.session_state['article_type'] = ''

def show():
    st.title("小学作文批改")

    # if st.button("开始新的批改"):
    #     st.session_state['page'] = 'primary_school_pkg'
    #     start_mark()
    #     st.experimental_rerun()
    if st.button("开始新的小学作文批改"):
        st.session_state['page'] = 'primary_school'
        start_primary_mark()
        st.experimental_rerun()
    if st.session_state['primary_marking'] == 'submitted':
        if st.button("查看刚才的批改"):
            st.session_state['page'] = 'primary_school'
            st.experimental_rerun()
    if st.button("查看小学作文库"):
        st.session_state['page'] = 'library'
        st.experimental_rerun()
    if st.button("上传作文图片"):
        st.session_state['page'] = 'newpic'
        st.experimental_rerun()
