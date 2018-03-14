# encoding: utf-8

"""
File: arrayset.py
Author: Rock Johnson
"""
from dataStructure.funtools.func import tostr
from dataStructure.arrays.arraybag import ArrayBag
from dataStructure.abstracts.abstractset import AbstractSet

class ArraySet(ArrayBag, AbstractSet):
    """基于array的set实现."""

    def __init__(self, sourceCollection=None):
        ArrayBag.__init__(self, sourceCollection)

    # 访问方法
    def __str__(self):
        """返回字符串."""
        return "(" + ", ".join(map(tostr, self)) + ")"

    # 赋值方法
    def add(self, item):
        """如果item不在self里,则将item添加到self里."""
        if not item in self:
            ArrayBag.add(self, item)