import streamlit as st

def start_senior_mark():
    st.session_state['senior_marking'] = 'working'
    st.session_state['senior_history'] = []
    st.session_state['senior_evaluation'] = []

def show():
    st.title("高中作文批改")

    if st.button("开始新的高中作文批改"):
        st.session_state['page'] = 'senior_high'
        start_senior_mark()
        st.experimental_rerun()
    if st.session_state['senior_marking'] == 'submitted':
        if st.button("查看刚才的批改"):
            st.session_state['page'] = 'senior_high'
            st.experimental_rerun()

