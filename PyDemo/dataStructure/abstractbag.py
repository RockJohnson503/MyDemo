# encoding: utf-8

"""
File: abstractbag.py
Author: Rock Johnson
"""
from dataStructure.arrays import Array
from dataStructure.abstractcollection import AbstractCollection

class AbstractBag(AbstractCollection):
    """bag数据结构的抽象类实现."""

    # 构造函数
    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        self._type = str(type(self))
        if "Linked" in self._type:  self._items = None
        elif "Array" in self._type: self._items = Array(0)
        AbstractCollection.__init__(self, sourceCollection)

    # 进行访问的方法
    def __str__(self):
        return "{" + ", ".join(map(str, self)) + "}"

    # 赋值的函数
    def clear(self):
        """使self变为空的."""
        self._size = 0
        if "Linked" in self._type:  self._items = None
        elif "Array" in self._type: self._items = Array(0)