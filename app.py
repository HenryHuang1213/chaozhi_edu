import streamlit as st
from primary_school_pkg import primary_school, primary_school_main
import lib_page
import main_page
import newpic_page
from junior_high_pkg import junior_high, junior_high_main
from senior_high_pkg import senior_high, senior_high_main


def main():
    st.set_page_config(page_title="学生作文批改")
    # st.title("作文批改")
    st.image('figure/study.jpg', width=350)

    if 'page' not in st.session_state:
        st.session_state['page'] = 'main_page'

    pages = {
        "main_page": main_page,
        "primary_school_main": primary_school_main,
        "junior_high_main": junior_high_main,
        "senior_high_main": senior_high_main,
        "library": lib_page,
        "primary_school": primary_school,
        "junior_high": junior_high,
        "senior_high": senior_high,
        "newpic": newpic_page
    }

    pages[st.session_state['page']].show()


if __name__ == "__main__":
    main()
