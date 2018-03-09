# encoding: utf-8

"""
File: arraystack.py
Author: Rock Johnson
"""
from dataStructure.abstracts.abstractstack import AbstractStack

class ArrayStack(AbstractStack):
    """基于array的stack实现"""

    # 构造函数
    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractStack.__init__(self, sourceCollection)

    # 进行访问的方法
    def __iter__(self):
        """支持将self进行迭代."""
        cursor = 0
        while cursor < self._size:
            yield self._items[cursor]
            cursor += 1

    def peek(self):
        """返回stack的顶部元素.
        前提: stack不是空的.
        如果是空的则抛出异常."""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        return self._items[len(self) - 1]

    # 赋值的函数
    def push(self, item):
        """将item插入stack的顶部."""
        self._items.add()
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """移除并返回stack的顶部元素.
        前提: stack不为空.
        Raises: KeyError如果stack为空.
        后置条件: 将顶部元素从stack中移除."""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        oldItem = self._items[len(self) - 1]
        self._size -= 1
        self._items.pop()
        return oldItem