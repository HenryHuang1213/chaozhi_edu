import json

import streamlit as st
from web_api import Teacher

if 'marking' not in st.session_state:
    st.session_state['marking'] = ''
if 'history' not in st.session_state:
    st.session_state['history'] = []
if 'evaluation' not in st.session_state:
    st.session_state['evaluation'] = []

def start_mark():
    st.session_state['marking'] = 'working'
    st.session_state['history'] = []
    st.session_state['evaluation'] = []
def show_example():
    requirements = '无'
    title = '我的姐姐'
    word_count = 300
    content = """
    大家好，很开心又跟大家见面了，钱不是主要原因，主要原因是我姐姐在学校门口潜我。从很远的地方，我就看见下她笑起来合不拢的大嘴和她的大白牙，跟手上向我摇晃的百元大钞，我就知道，她又要收买我了。
    我的姐姐很墨迹。一家人约好了早上7点出门，8点了我们还在家里，妈妈催她快点，她就一边描眉一边嘟嘟：“求您了，再等我个五分钟。”她一直跟我强调说则幅眼前过，不泡是罪过，每天努力地泡帅哥。
    我的姐姐曾经为了民族团结，硬要背上氧气瓶，去西藏找丁真和亲，还问妈妈嫁远了能支持吗，我妈让她滚一边做梦去。后来才知道人家了真是四川的。
    喊她吃饭也不起，她想吃的东西通常活不过第二天，回奶奶家想吃鸡肉，想就一直说鸡啄她，鸡当天晚上就上桌了。
    现在每天晚上除了写作业，还得给她写一篇作文。她现在正跟鬼一样追在我后面问：“写完没？写完没？这么慢，打电报都比你快，这不行，得扣钱！谁都别想阻止我出道！”
    唉，我是真的真的很无语。
    """
    return requirements, title, word_count, content

st.set_page_config(page_title="学生作文批改")
st.title("小学作文批改")
st.image('figure/study.jpg', width=350)

chat_button = st.button("开始新的批改", on_click=start_mark)

def print_evaluation():
    response = st.session_state['evaluation']
    st.markdown(f"*作文题目:*  {response['作文题目']}")
    st.markdown(f"*核心内容:*  {response['作文核心内容']}")
    st.markdown(f"*亮点:*  {response['亮点']}")
    st.markdown(f"*错别字:*  {response['错别字']}")
    st.markdown(f"*病句:*  {response['病句']}")
    st.markdown(f"*好句:*  {response['好句']}")
    st.markdown(f"*点评:*  {response['点评']}")
    st.markdown("*评分:*")

    total_score = sum([i['评分'] for i in response['评分'].values()])
    st.markdown(f"    总分: {total_score}")
    for k, v in response['评分'].items():
        st.markdown(f"    {k}: {v['理由']}")



def submit_func(requirements, title, word_count, content):
    if requirements == '':
        requirements = '无'
    st.markdown(f"**作文要求:** {requirements}")
    st.markdown(f"**作文题目:** 《{title}》")
    st.markdown(f"**作文字数:** {word_count}")
    st.markdown(f"**作文正文:**\n\n {content}")
    st.markdown('**作文评价:**')
    print_evaluation()
    st.session_state['history'] = [requirements, title, word_count, content]

def get_evaluation(requirements, title, word_count, content):
    evaluation = Teacher.get_eval(requirements, title, word_count, content)
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
            example_button = st.form_submit_button(label='示例批改')
            # st.session_state['history'] = [requirements_input, title_input, word_count_input, content_input]
    if submit_button:
        st.session_state['marking'] = 'submitted'
        get_evaluation(requirements_input, title_input, word_count_input, content_input)
        submit_func(requirements_input, title_input, word_count_input, content_input)
        st.experimental_rerun()
    elif example_button:
        st.session_state['marking'] = 'submitted'
        requirements, title, word_count, content = show_example()
        get_evaluation(requirements, title, word_count, content)
        submit_func(requirements, title, word_count, content)
        st.experimental_rerun()

elif st.session_state['marking'] == 'submitted':
    submit_func(*st.session_state['history'])

