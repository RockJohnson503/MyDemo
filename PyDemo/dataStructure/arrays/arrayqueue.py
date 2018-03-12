# encoding: utf-8

"""
File: arrayqueue.py
Author: Rock Johnson
"""
from dataStructure.abstracts.abstractqueue import AbstractQueue

class ArrayQueue(AbstractQueue):
    """基于array的queue实现."""

    # 构造函数
    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractQueue.__init__(self, sourceCollection)

    # 进行访问的方法
    def peek(self):
        """返回queue的队头项.
        前提: queue不是空的.
        如果是空的则抛出异常."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
        return self._items[0]

    # 赋值的函数
    def add(self, item):
        """将item插入queue的队尾."""
        self._items.add()
        self._items[len(self)] = item
        self._size += 1

    def pop(self):
        """移除并返回queue的队头项.
        前提: queue不为空.
        Raises: KeyError如果queue为空.
        后置条件: 将队头项从queue中移除."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
        oldItem = self._items[0]
        for i in range(len(self) - 1):
            self._items[i] = self._items[i + 1]
        self._size -= 1
        self._items.pop()
        return oldItem