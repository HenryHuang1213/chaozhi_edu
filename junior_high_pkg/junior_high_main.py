import streamlit as st

def start_junior_mark():
    st.session_state['junior_marking'] = 'working'
    st.session_state['junior_history'] = []
    st.session_state['junior_evaluation'] = []

def show():
    st.title("初中作文批改")

    if st.button("开始新的初中作文批改"):
        st.session_state['page'] = 'junior_high'
        start_junior_mark()
        st.experimental_rerun()
    if st.session_state['junior_marking'] == 'submitted':
        if st.button("查看刚才的批改"):
            st.session_state['page'] = 'junior_high'
            st.experimental_rerun()

    if st.button("上传作文图片"):
        st.session_state['page'] = 'junior_pic_page'
        st.experimental_rerun()


