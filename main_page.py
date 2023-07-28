import streamlit as st
import os
import random






def show():
    st.title("作文批改")
    if 'primary_marking' not in st.session_state:
        st.session_state['primary_marking'] = ''
    if 'primary_history' not in st.session_state:
        st.session_state['primary_history'] = []
    if 'junior_marking' not in st.session_state:
        st.session_state['junior_marking'] = ''
    if 'junior_history' not in st.session_state:
        st.session_state['junior_history'] = []
    if 'senior_marking' not in st.session_state:
        st.session_state['senior_marking'] = ''
    if 'senior_history' not in st.session_state:
        st.session_state['senior_history'] = []

    if 'primary_evaluation' not in st.session_state:
        st.session_state['primary_evaluation'] = []
    if 'junior_evaluation' not in st.session_state:
        st.session_state['junior_evaluation'] = []
    if 'senior_evaluation' not in st.session_state:
        st.session_state['senior_evaluation'] = []

    if 'article_type' not in st.session_state:
        st.session_state['article_type'] = ''
    if 'random_id' not in st.session_state:
        random_number = random.randint(10000000, 99999999)
        while os.path.exists(f'zuowen/{random_number}.jpg'):
            random_number = random.randint(10000000, 99999999)
        st.session_state['random_id'] = random_number
    if 'Evaluation_Cost_Time' not in st.session_state:
        st.session_state['Evaluation_Cost_Time'] = 0

    # if st.button("开始新的批改"):
    #     st.session_state['page'] = 'primary_school_pkg'
    #     start_mark()
    #     st.experimental_rerun()
    if st.button("批改小学作文"):
        st.session_state['page'] = 'primary_school_main'
        st.experimental_rerun()
    if st.button("批改初中作文"):
        st.session_state['page'] = 'junior_high_main'
        st.experimental_rerun()
    if st.button("批改高中作文"):
        st.session_state['page'] = 'senior_high_main'
        st.experimental_rerun()

