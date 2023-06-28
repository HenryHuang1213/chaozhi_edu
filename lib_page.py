import json

import streamlit as st
from parse_csv import Parse_CSV
from web_api import Teacher

def show():
    # st.title("Library")
    st.title("素材库")
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


    p_c = Parse_CSV()

    page = st.sidebar.selectbox("选择素材类型", ("作文", "周记"))
    if page == "作文":
        with st.container():
            with st.form(key='my_form1'):
                article_data = p_c.get_article_data()
                article_index = st.selectbox("选择作文编号", (range(1, len(article_data) + 1)))
                if st.form_submit_button(label='查看'):
                    requirement = article_data[article_index - 1][0]
                    if requirement:
                        st.markdown(f"**作文要求:** {requirement}")
                    title = article_data[article_index - 1][1]
                    if title:
                        st.markdown(f"**作文题目:** 《{title}》")
                    word_count = article_data[article_index - 1][2]
                    if word_count:
                        st.markdown(f"**作文字数:** {word_count}")
                    st.markdown(f"**作文正文:** \n\n{article_data[article_index - 1][3]}")

    elif page == "周记":
        with st.container():
            with st.form(key='my_form2'):
                article_data = p_c.get_note_data()
                article_index = st.selectbox("选择周记编号", (range(1, len(article_data)+1)))
                if st.form_submit_button(label='查看'):
                    st.markdown(f"**周记正文:** \n\n{article_data[article_index - 1]}")
