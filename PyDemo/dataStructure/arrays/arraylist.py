# encoding: utf-8

"""
File: arraylist.py
Author: Rock Johnson
"""
from dataStructure.arrays.arraylistiterator import ArrayListIterator
from dataStructure.abstracts.abstractlist import AbstractList

class ArrayList(AbstractList):
    """基于array的list实现."""

    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractList.__init__(self, sourceCollection)

    # 访问函数
    def __getitem__(self, i):
        """前提: 0 <= i < len(self)
        返回索引i的item.
        Raises: IndexError."""
        if i < 0 or i >=len(self):
            raise IndexError("list index out of range")
        cursor = 0
        for item in self:
            if cursor == i:
                return item
            cursor += 1

    # 赋值函数
    def __setitem__(self, i, value):
        """前提: 0 <= i < len(self)
        将索引i的值替换成value.
        Raises: IndexError."""
        if i < 0 or i >=len(self):
            raise IndexError("list index out of range")
        cursor = 0
        for item in self:
            if cursor == i:
                item = value
                break
            cursor += 1

    def insert(self, i, item):
        """将item插入索引i的位置."""
        # 调整数组大小
        self._items.add()
        if i < 0 : i = 0
        elif i > len(self): i = len(self)
        if i < len(self):
            for j in range(len(self), i, -1):
                self._items[j] = self._items[j - 1]
        self._items[i] = item
        self._size += 1
        self.incModCount()

    def pop(self, i=None):
        """前提: 0 <= i < len(self).
        移除并返回索引i位置的值.
        如果i = None, 就给i个默认值len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("list index of list")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self.incModCount()
        # 调整数组大小
        self._items.pop()
        return item

    def listIterator(self):
        """返回列表迭代器."""
        return ArrayListIterator(self)