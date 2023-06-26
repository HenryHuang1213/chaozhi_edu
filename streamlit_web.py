import json

import streamlit as st
from web_api import Teacher
import sample_article

if 'marking' not in st.session_state:
    st.session_state['marking'] = ''
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'evaluation' not in st.session_state:
    st.session_state['evaluation'] = []
if 'article_type' not in st.session_state:
    st.session_state['article_type'] = ''

def start_mark():
    st.session_state['marking'] = 'working'
    st.session_state['history'] = []
    st.session_state['evaluation'] = []
    st.session_state['article_type'] = ''



st.set_page_config(page_title="学生作文批改")
st.title("小学作文批改")
st.image('figure/study.jpg', width=350)

chat_button = st.button("开始新的批改", on_click=start_mark)

def print_article_evaluation():
    response = st.session_state['evaluation']
    st.markdown(f"*作文题目:*  《{response['作文题目']}》")
    st.markdown(f"*核心内容:*  {response['作文核心内容']}")
    st.markdown(f"*亮点:*  {response['亮点']}")
    st.markdown(f"*错别字:*  {response['错别字']}")
    st.markdown(f"*病句:*  ")
    # 病句: {'病句总数': 3, '病句内容': {'1': {'病句内容': '它因为它一继续笑着说：“亲爱的乌鸦，您的孩子好吗？”', '病句问题': '成分残缺', '修改意见': '它一直笑着说：“亲爱的乌鸦，您的孩子好吗？”'}, '2': {'病句内容': '乌鸦看了狐狸一眼，还是没有回答它。', '病句问题': '用词不当', '修改意见': '乌鸦看了狐狸一眼，还是没有回答它的话。'}, '3': {'病句内容': '可乌鸦现在这么聪明，狐狸就想爬上树去抢那块肉。', '病句问题': '概念不清', '修改意见': '但乌鸦现在这么聪明，狐狸就想爬上树去抢那块肉。'}}}
    if response['病句']['病句总数']:
        for i in range(1, response['病句']['病句总数']+1):
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{i}:")
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;病句内容：{response['病句']['病句内容'][str(i)]['病句内容']}")
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;病句问题：{response['病句']['病句内容'][str(i)]['病句问题']}")
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;修改意见：{response['病句']['病句内容'][str(i)]['修改意见']}")
    # wrong_sentense = response['病句'].split('。')
    st.markdown(f"*好句:* ")
    # 好句:{'好句总数': 2, '好句内容': {'1': {'好句内容': '乌鸦假装更得意了，把肉叼回巢里，抖抖翅膀，准备放声歌唱。', '点评': '描写细腻，生动形象。'}, '2': {'好句内容': '从此以后，它又变成了一个善良的狐狸。', '点评': '简洁明了，表达深刻。'}}}
    if response['好句']['好句总数']:
        for i in range(1, response['好句']['好句总数']+1):
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{i}:")
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;好句内容：{response['好句']['好句内容'][str(i)]['好句内容']}")
            st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;点评：{response['好句']['好句内容'][str(i)]['点评']}")
    st.markdown(f"*全文点评:*  {response['点评']}")
    st.markdown("*评分:*")

    total_score = sum([i['评分'] for i in response['评分'].values()])
    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;总分: {total_score}")
    full_score = ['10','15','15','15','15','15','15']
    for k, v in response['评分'].items():
        st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;{k}:")
        st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;分数：{v['评分']} / {full_score.pop(0)}")
        st.write(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;理由：{v['理由']}")


def count_words(content):
    return len(content)

def submit_func(requirements, title, word_count, content):
    if word_count == '' or word_count == 0:
        word_count = count_words(content)
    if st.session_state['article_type'] == 'note':
        st.markdown(f"**作文类型:** 周记")
        st.markdown(f"**作文正文:** {content}")
        st.markdown('**作文评价:**')
        st.write('内容正在推出中...')
    else:
        if requirements == '':
            requirements = '无'
        st.markdown(f"**作文要求:** {requirements}")
        st.markdown(f"**作文题目:** 《{title}》")
        st.markdown(f"**作文字数:** {word_count}")
        st.markdown(f"**作文正文:** {content}")
        st.markdown('**作文评价:**')
        print_article_evaluation()
    st.session_state['history'] = [requirements, title, word_count, content]

def get_evaluation(requirements, title, word_count, content):
    if requirements_input == '' and title_input == '' and word_count_input == 0:
        evaluation = Teacher.get_note_eval(content)
        st.session_state['article_type'] = 'note'
    else:
        evaluation = Teacher.get_article_eval(requirements, title, word_count, content)
        st.session_state['article_type'] = 'article'
    st.session_state['evaluation'] = json.loads(evaluation)


if st.session_state['marking'] == 'working':
    with st.container():
        with st.form(key='my_form'):
            requirements_input = st.text_input(label='请输入作文要求')
            title_input = st.text_input(label='请输入作文题目')
            word_count_input = st.number_input(label='请输入作文字数', min_value=0)
            content_input = st.text_area(label='请输入作文正文', height=200)

            # 每个form都需要一个按钮来提交表单
            submit_button = st.form_submit_button(label='提交')
            example1_button = st.form_submit_button(label='示例批改1')
            example2_button = st.form_submit_button(label='示例批改2')
            # st.session_state['history'] = [requirements_input, title_input, word_count_input, content_input]
    temp = 0
    if submit_button:
        st.session_state['marking'] = 'submitted'
        temp = 1
    elif example1_button:
        st.session_state['marking'] = 'submitted'
        requirements_input, title_input, word_count_input, content_input = sample_article.show_example1()
        temp = 1
    elif example2_button:
        st.session_state['marking'] = 'submitted'
        requirements_input, title_input, word_count_input, content_input = sample_article.show_example2()
        temp = 1

    if temp:
        get_evaluation(requirements_input, title_input, word_count_input, content_input)
        submit_func(requirements_input, title_input, word_count_input, content_input)
        st.experimental_rerun()

elif st.session_state['marking'] == 'submitted':
    submit_func(*st.session_state['history'])

