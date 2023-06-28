import json

import openai

from article_prompt import ArticlePrompt
from notes_prompt import NotesPrompt


class Teacher:

    @staticmethod
    def get_completion(prompt, model="gpt-4"):
        openai.api_key_path = "api.key"
        messages = [{"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    @staticmethod
    def get_text(num):
        num = str(num)
        with open("document/article" + num + ".txt", "r", encoding="utf-8") as f:
            text = f.read()
        return text

    @classmethod
    def get_article_eval(cls, requirements, title, word_count, content):

        a_prompt = ArticlePrompt(requirements, title, word_count, content)
        prompt = a_prompt.get_prompt()
        # print(prompt)
        response = cls.get_completion(prompt)
        return response

    @classmethod
    def get_note_eval(cls, content):
        return '{}'
        # n_prompt = NotesPrompt(content)
        # prompt = n_prompt.get_prompt()
        # # print(prompt)
        # response = cls.get_completion(prompt)
        # return response

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


# def show_example():
#     requirements = '无'
#     title = '狐狸和乌鸦新编'
#     word_count = ''
#     content = """
#     森林里有一棵古老的大树，树枝上有一个乌鸦的家。下面的树洞里住着一只狐狸。
#     有一天，乌鸦叼回来一块肉，得意地站在树枝上。狐狸看见了，忍不住流出口水，心想：“哇，那块肉一定很好吃，要是能咬上一口，该多好呀！”狐狸想了一会儿，想出一个主意。它咽了咽口水，笑着对乌鸦说：“亲爱的乌鸦，你好吗？”
#     乌鸦眼就识破了狐狸的诡计，没有回答狐狸。它因为它一继续笑着说：“亲爱的乌鸦，您的孩子好吗？”乌鸦看了狐狸一眼，还是没有回答它。狐狸见乌鸦还是没回答，就说：“亲爱的乌鸦小姐，您的羽毛真漂亮，就连孔雀和你比起来都差远了！”
#     乌鸦假装高兴，狐狸以为乌鸦快要上当了，就摇摇尾巴说：“您的嗓子真好，大家都爱听您唱歌，您就唱几句吧！”乌鸦假装更得意了，把肉叼回巢里，抖抖翅膀，准备放声歌唱。
#     狐狸本想借唱歌的理由，让乌鸦张嘴使肉掉下来，趁机叼走的。可乌鸦现在这么聪明，狐狸就想爬上树去抢那块肉。但它不会爬树，爬到一半就摔下来了。狐狸再也不敢骗乌鸦了，它明白骗人是不好的。
#     从此以后，它又变成了一个善良的狐狸。
#     """
#     return requirements, title, word_count, content
#
# requirements, title, word_count, content = show_example()
# temp = Teacher().get_article_eval(requirements, title, word_count, content)
# print(temp)
# with open('test.json', 'w', encoding='utf-8') as f:
#     f.write(temp)
# j_s = json.loads(temp)
# print(j_s)
# print(type(temp))
# print(temp)
# dict_temp = eval(temp)
# print(type(dict_temp))
# print(dict_temp)
# print(dict_temp['评分'].values())
# print([i['评分'] for i in dict_temp['评分'].values()])