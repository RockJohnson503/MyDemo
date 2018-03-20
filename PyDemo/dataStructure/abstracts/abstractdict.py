# encoding: utf-8

"""
File: abstractdict.py
Author: Rock Johnson
"""
from dataStructure.funtools.func import tostr
from dataStructure.abstracts.abstractcollection import AbstractCollection

class AbstractDict(AbstractCollection):
    """dict数据结构的抽象类实现"""

    def __init__(self, sourceCollection=None):
        """如果存在,则将item从sourceCollection复制到集合中."""
        AbstractCollection.__init__(self)

    def __str__(self):
        """返回字符串."""
        return "{" + ", ".join(map(str, self.items())) + "}"

    def __add__(self, other):
        """返回一个包含self和other的内容的新字典."""
        result = type(self)(map(lambda item: (item.key, item.value), self.items()))
        for key in other:
            result[key] = other[key]
        return result

    def __eq__(self, other):
        """如果self等于other,返回Ture,否则返回False."""
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other):
            return False
        for key1, key2 in zip(self, other):
            if key1 != key2:
                return False
        return True

    def keys(self):
        """返回字典中键的迭代器."""
        return iter(self)

    def values(self):
        """返回字典中值的迭代器."""
        return iter(map(lambda key: self[key], self))

    def items(self):
        """返回字典中键值对的迭代器."""
        return iter(map(lambda key: "(" + tostr(key) + ", " + tostr(self[key]) + ")", self))

class Item(object):
    """代表一个字典item.支持按键比较."""

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return tostr(self.key) + ": " + tostr(self.value)

    def __eq__(self, other):
        if type(self) != type(other): return False
        return self.key == other.key

    def __lt__(self, other):
        if type(self) != type(other): return False
        return self.key < other.key

    def __le__(self, other):
        if type(self) != type(other): return False
        return self.key <= other.key