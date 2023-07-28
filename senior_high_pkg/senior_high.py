
import streamlit as st


def show():
    st.title("高中作文批改")
    if st.button("回到主页"):
        st.session_state['page'] = 'main_page'
        st.experimental_rerun()
    if st.button("回到高中批改主页"):
        st.session_state['page'] = 'senior_high_main'
        st.experimental_rerun()
