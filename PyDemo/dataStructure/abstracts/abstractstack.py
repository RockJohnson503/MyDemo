# encoding: utf-8

"""
File: abstractstack.py
Author: Rock Johnson
"""
from dataStructure.funtools.func import tostr
from dataStructure.abstracts.abstractcollection import AbstractCollection

class AbstractStack(AbstractCollection):
    """stack数据结构的抽象类实现."""

    # 构造函数
    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractCollection.__init__(self, sourceCollection)

    # 进行访问的方法
    def __str__(self):
        """返回字符串."""
        mid = " ".join(map(tostr, self))
        if mid == "":
            mid = "None"
        return mid

    # 赋值的函数
    def add(self, item):
        """将item添加进self."""
        self.push(item)