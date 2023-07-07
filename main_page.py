import streamlit as st


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
