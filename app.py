import streamlit as st
import streamlit_web
import lib_page
import main_page

def main():
    st.set_page_config(page_title="学生作文批改")
    st.title("小学作文批改")
    st.image('figure/study.jpg', width=350)

    if 'page' not in st.session_state:
        st.session_state['page'] = 'main_page'

    pages = {
            "main_page": main_page,
            "library": lib_page,
            "eval":streamlit_web
        }

    pages[st.session_state['page']].show()

if __name__ == "__main__":
    main()
