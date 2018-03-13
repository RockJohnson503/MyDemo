# encoding: utf-8

"""
File: arraylist.py
Author: Rock Johnson
"""
from dataStructure.arrays.arraysortedlist import ArraySortedList

class ArrayList(ArraySortedList):
    """基于array的list实现."""

    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        ArraySortedList.__init__(self, sourceCollection)

    # 访问函数
    def index(self, item):
        """前提: item在self里面.
        返回item的索引.
        异常: 如果item不在self里面则抛出KeyError异常."""
        for position, data in enumerate(self):
            if data == item:
                return position
        raise ValueError(str(item) + "Not in list.")

    # 赋值函数
    def add(self, item):
        """将item添加到self里面."""
        self.insert(len(self), item)

    def append(self, item):
        """将item添加到self的末尾."""
        self.insert(len(self), item)

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