
class ArticlePrompt:

    def __init__(self, requirements, title, word_count, content):
        self.requirements = requirements
        self.title = title
        self.word_count = word_count
        self.content = content



    def get_prompt(self):
        json_format = """{
    "作文题目": <题目>,
    "作文核心内容": <列出整理的"作文核心内容">,
    "亮点": <列出整理的"亮点">,
    "错别字": <列出整理的具体的"错别字">,
    "病句": {
        "病句总数": <病句总数>,
        "病句内容": {
            <病句序号>: {
                    "病句内容": <病句内容>,
                    "病句问题": <描述问题>,
                    "修改意见": <提供修改意见>，}
        },
    },
    "好句": {
        "好句总数": <好句总数>,
        "好句内容": {
            "<好句序号>": {
                "好句内容": <好句内容>,
                "点评": <点评>}
        },
        }
    },
    "点评": <点评内容>,
    "评分": {
        "作文题目": {
            "评分": <分数>,
            "理由"： <评分理由>
        },
        "文章主题": {
            "评分": <分数>,
            "理由"： <评分理由>
        },
        "切题": {
            "评分": <分数>,
            "理由"： <评分理由>
        },
        "逻辑思维": {
            "评分": <分数>,
            "理由"： <评分理由>
        },
        "语句运用": {
            "评分": <分数>,
            "理由"： <评分理由>
        },
        "文字使用": {
            "评分": <分数>,
            "理由"： <评分理由>
        },
        "字数": {
            "评分": <分数>,
            "理由"： <评分理由>
        }
    }
}"""

        prompt = f"""
    你将收到一篇文章，内容在两组三个反引号中间。
    你的身份是小学语文老师
    你的性格是和蔼可亲，认真严谨
    你的任务是评判小学作文

    你首先需要完成以下步骤：
        1 - 阅读文章，并概括主题和中心思想。
        2 - 标记文中错别字和病句并记录，语句不通顺也算入病句
        3 - 根据作文要求，判断作文题目和内容是否切题
        4 - 判断文章内容与题目是否契合
        5 - 判断文章是否分段清晰，逻辑顺畅
        6 - 统计文章正文字数
        7 - 给予点评，简要概括优点和缺点    

    在给出回复前，请先整理以下内容：
        "作文核心内容": 一句话概括作文中心思想和主要内容,20字以上
        "亮点": 点评文中亮点内容，如使用特别的修辞、优美的语句、引用名言等,
        "错别字": 列举文中的错别字，并指出正确答案,
        "病句": 依此整理文中的病句，并指出语病，进行修改,
        "好句": 列举一到两句文中优秀的句子,如使用特别的修辞手法、优美的句式等。好句不能跟病句重复，好句中如果出现错别字，显示正确的语句,
        "点评": 综合全文，给出点评内容,

    你的打分评分标准：
        1、作文题目 (10分)：
            评判标准：题目恰当
            评分细则：
                - 如果规定作文题目：不扣分
                - 如果没有信息是否规定作文题目：根据作文题目是否得体进行评分。优秀题目，得10分。普通题目，得8分。恶意题目，得0分。
                - 如果给出作文题目大致范畴：根据是否切题进行评分。紧扣题目，得10分。部分延申，得10分。延申过多，得7分。完全偏题，得5分。
                - 如果没有给出任何信息：题目与文章内容保持一致，得10分。题目与文章内容相去甚远，得5分。
                - 没有题目：得0分。
        2、文章主题 (15分)：
            评判标准：思想健康，中心明确
            评分细则：
                - 文章的主题思想是否健康：总结出中心思想，根据文章的主题思想是否健康积极向上，给出评分。
                - 中心内容是否明确：根据文章的中心内容是否明确，给出评分。
                - 判断依据可以是文章主题的连贯性和文章主旨的突出。
        3、切题 (15分)：
            评判标准：内容与题目相符，描写具体、生动
            评分细则：
                - 文章的内容是否与题目相符，描述是否具体和生动，每有一处不符合要求的，扣一分，最多扣5分。
        4、逻辑思维 (15分)：
            评判标准：条理清楚，段落分明
            评分细则：
                - 文章是否条理清楚，段落是否分明，每缺一项扣5分。
        5、语句运用 (15分)：
            评判标准：语句通顺
            评分细则：
                - 文章的语句是否通顺，每发现一处语句不通的，扣1分，最多扣5分。
        6、文字使用(15分)：
            评判标准：会用标点，错别字少 
            评分细则：
                - 检查标点符号的使用和错别字的数量，每两个错别字扣1分，最多扣5分；每五处标点错误扣1分，最多扣5分。
        7、字数 (15分)：
            评判标准：字数基本符合要求
            评分细则：
                - 如果明确规定字数要求：达到90%以上得15分。不足90%，达到80%以上得10分。不足80%，达到60%，得5分。不足60%，得0分。
                - 如果没有明确规定字数：得15分。


    使用json格式给我回复
    json文件格式和内容如下：
    {json_format}

    【文章】: 
    '''
    作文要求：{self.requirements}
    作文题目：{self.title}
    字数要求：{self.word_count}
    作文内容：{self.content}
    '''

    """
        return prompt


    # 你需要学习小学语文病句类型：
    #     1 - 成分残缺 ： 句子里缺少了某些必要的成分，意思表达就不完整，不明确。
    #     2 - 用词不当 ： 由于对词义理解不清，就容易在词义范围大小、褒贬等方面用得不当，特别是近义词，关联词用错，造成病句。
    #     3 - 词语搭配不当 ： 在句子中某些词语在意义上不能相互搭配或者是搭配起来不合事理，违反了语言的习惯，造成了病句。包括一些关联词语的使用不当。
    #     4 - 前后矛盾 ： 在同一个句子中，前后表达的意思自相矛盾，造成了语意不明。
    #     5 - 词序颠倒 ： 在一般情况下，一句话里面的词序是固定的，词序变了，颠倒了位置，句子的意思就会发生变化，甚至造成病句。
    #     6 - 重复罗嗦 ： 在句子中，所用的词语的意思重复了，显得罗嗦累赘。
    #     7 - 概念不清 ： 指句子中词语的概念不清，属性不当，范围大小归属混乱。
    #     8 - 不合逻辑不合事理 ： 句子中某些词语概念不清，使用错误，或表达的意思不符合事理，也易造成病句。
    #     9 - 指代不明 ： 指句子中出现多个人或状物时，指代不明确，含混不清。