import json

import streamlit as st
from .junior_web_api import Teacher
from . import junior_sample_article

def print_article_evaluation():
    st.write(f"Evaluation_Cost_Time : {st.session_state['Evaluation_Cost_Time']}")

    response = st.session_state['junior_evaluation']
    st.markdown(f"*作文题目:*  《{response['作文题目']}》")
    st.markdown(f"*核心内容:*  {response['作文核心内容']}")
    st.markdown(f"*亮点:*  {response['亮点']}")
    st.markdown(f"*错别字:*  ")
    if response['错别字']['错别字总数']:
        for i in range(1, response['错别字']['错别字总数'] + 1):
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{i}:")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;错别字：{response['错别字']['错别字内容'][str(i)]['错别字']}")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;原句：{response['错别字']['错别字内容'][str(i)]['原句']}")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;正确字：{response['错别字']['错别字内容'][str(i)]['正确字']}")
    st.markdown(f"*病句:*  ")
    if response['病句']['病句总数']:
        for i in range(1, response['病句']['病句总数'] + 1):
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{i}:")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;病句内容：{response['病句']['病句内容'][str(i)]['病句内容']}")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;病句问题：{response['病句']['病句内容'][str(i)]['病句问题']}")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;修改意见：{response['病句']['病句内容'][str(i)]['修改意见']}")
    st.markdown(f"*好句:* ")
    if response['好句']['好句总数']:
        for i in range(1, response['好句']['好句总数'] + 1):
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{i}:")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;好句内容：{response['好句']['好句内容'][str(i)]['好句内容']}")
            st.write(
                f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;点评：{response['好句']['好句内容'][str(i)]['点评']}")
    st.markdown(f"*全文点评:*  {response['点评']}")
    st.markdown("*评分:*")

    total_score = sum([i['评分'] for i in response['评分'].values()])
    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;总分: {total_score}")
    full_score = ['5', '8', '8', '8', '8', '8', '5']
    for k, v in response['评分'].items():
        st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{k}:")
        st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分数：{v['评分']} / {full_score.pop(0)}")
        st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;理由：{v['理由']}")



def count_words(content):
    return len(content)


def submit_func(requirements, title, word_count, content):
    if word_count == '' or word_count == 0:
        word_count = count_words(content)

    if requirements != '':
        st.markdown(f"**作文要求:** {requirements}")
    if title != '':
        st.markdown(f"**作文题目:** 《{title}》")
    if word_count != 0:
        st.markdown(f"**作文字数:** {word_count}")
    st.markdown(f"**作文正文:** {content}")
    st.markdown('**作文评价:**')
    print_article_evaluation()
    st.session_state['junior_history'] = [requirements, title, word_count, content]


def get_evaluation(requirements, title, word_count, content):
    evaluation = Teacher.get_article_eval(requirements, title, word_count, content)
    st.session_state['article_type'] = 'article'
    # print(evaluation)
    st.session_state['junior_evaluation'] = json.loads(evaluation)


def article_insert_container():
    with st.container():
        with st.form(key='my_form'):
            requirements_input = st.text_input(label='请输入作文要求', value='')
            title_input = st.text_input(label='请输入作文题目', value='')
            word_count_input = st.number_input(label='请输入作文字数', min_value=0, value=0)
            content_input = st.text_area(label='请输入作文正文', height=200, value='')

            submit_button = st.form_submit_button(label='提交')
            example1_button = st.form_submit_button(label='示例批改1')
            example2_button = st.form_submit_button(label='示例批改2')
            example3_button = st.form_submit_button(label='示例批改3')
            # st.session_state['junior_history'] = [requirements_input, title_input, word_count_input, content_input]
    temp = 0
    if submit_button:
        st.session_state['junior_marking'] = 'submitted'
        temp = 1
    elif example1_button:
        st.session_state['junior_marking'] = 'submitted'
        requirements_input, title_input, word_count_input, content_input = junior_sample_article.show_example1()
        temp = 1
    elif example2_button:
        st.session_state['junior_marking'] = 'submitted'
        requirements_input, title_input, word_count_input, content_input = junior_sample_article.show_example2()
        temp = 1
    elif example3_button:
        st.session_state['junior_marking'] = 'submitted'
        requirements_input, title_input, word_count_input, content_input = junior_sample_article.show_example3()
        temp = 1


    if temp:
        get_evaluation(requirements_input, title_input, word_count_input, content_input)
        submit_func(requirements_input, title_input, word_count_input, content_input)
        st.experimental_rerun()



def show():
    st.title("初中作文批改")
    if st.button("回到主页"):
        st.session_state['page'] = 'main_page'
        st.experimental_rerun()
    if st.button("回到初中批改主页"):
        st.session_state['page'] = 'junior_high_main'
        st.experimental_rerun()

    if st.session_state['junior_marking'] == 'working':
        article_insert_container()

    elif st.session_state['junior_marking'] == 'submitted':
        if st.session_state['junior_history'] != []:
            submit_func(*st.session_state['junior_history'])
        else:
            st.write('本次提交网络错误，请重新开始新的批改')
