# encoding: utf-8

"""
File: testpaper.py
Author: Rock Johnson
"""
class TestPaper:
    def test_question_1(self):
        print('杨过得到,后来个了郭靖,炼成倚天剑、屠龙刀的玄铁可能是 [ ]\na.球墨铸铁\tb.马口铁\tc.高速合金钢\td.碳素纤维')
        print('答案: ', self.answer_1())

    def test_question_2(self):
        print('杨过、程英、陆无双铲除了情花,造成 [ ]\na.使这种植物不再害人\tb.使一种珍稀物种灭绝\tc.破坏了那个生物圈的生态平衡\td.造成该地区沙漠化')
        print('答案: ', self.answer_2())

    def test_question_3(self):
        print('蓝凤凰致使华山师徒、桃谷六仙呕吐不止,如果你是大夫,会给他们开什么药 [ ]\na.阿司匹林\tb.牛黄解毒片\tc.氟哌酸\td.让他们喝大量的生牛奶\te.以上全不对')
        print('答案: ', self.answer_3())

    def answer_1(self):
        return ''

    def answer_2(self):
        return ''

    def answer_3(self):
        return ''


class TestPaperA(TestPaper):
    def answer_1(self):
        return 'a'

    def answer_2(self):
        return 'b'

    def answer_3(self):
        return 'b'


class TestPaperB(TestPaper):
    def answer_1(self):
        return 'd'

    def answer_2(self):
        return 'c'

    def answer_3(self):
        return 'a'


if __name__ == '__main__':
    a = TestPaperA()
    b = TestPaperB()
    a.test_question_1()
    a.test_question_2()
    a.test_question_3()
    print('==========================')
    b.test_question_1()
    b.test_question_2()
    b.test_question_3()