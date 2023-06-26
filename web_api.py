
import openai

from article_prompt import ArticlePrompt
from notes_prompt import NotesPrompt


class Teacher:

    @staticmethod
    def get_completion(prompt, model="gpt-3.5-turbo"):
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
# temp = Teacher().get_eval(requirements, title, word_count, content)
# print(type(temp))
# print(temp)
# dict_temp = eval(temp)
# print(type(dict_temp))
# print(dict_temp)
# print(dict_temp['评分'].values())
# print([i['评分'] for i in dict_temp['评分'].values()])