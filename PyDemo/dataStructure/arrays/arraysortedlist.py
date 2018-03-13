# encoding: utf-8

"""
File: arraysortedlist.py
Author: Rock Johnson
"""
from dataStructure.abstracts.abstractlist import AbstractList

class ArraySortedList(AbstractList):
    """基于array实现的排序list."""

    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractList.__init__(self, sourceCollection)

    # 访问函数
    def __getitem__(self, i):
        """前提: 0 <= i < len(self)
        返回索引i的item.
        Raises: IndexError."""
        return self._items[i]

    # 赋值函数
    def __setitem__(self, i, value):
        """前提: 0 <= i < len(self)
        将索引i的值替换成value.
        Raises: IndexError."""
        if i < 0 or i >= len(self):
            raise IndexError("list index out of range")
        self._items[i] = value

    def __contains__(self, item):
        """如果item在self里面则返回True否则返回False"""
        self.index(item, "bool")

    def index(self, item, retype="int", isadd=False):
        """返回self里的item,如果item不在里面则返回-1
        retype: 指定返回的类型(int, bool),默认int
        isadd: 专门为add添加的判断属性"""
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if not isadd and self._items[mid] == item:
                if retype == "int":
                    return mid
                elif retype == "bool":
                    return True
            elif isadd and self._items[mid] <= item and self._items[mid + 1] >= item:
                return mid + 1
            elif self._items[mid] > item:
                right = mid - 1
            else:
                left = mid + 1
        if isadd:
            return 0
        elif retype == "int":
            return -1
        elif retype == "bool":
            return False

    # 赋值的函数
    def add(self, item):
        """将item添加到self里面."""
        self._items.add()
        targetIndex = 0
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            targetIndex = len(self)
        else:
            targetIndex = self.index(item, isadd=True)
            for i in range(len(self._items) - 1, targetIndex, -1):
                self._items[i] = self._items[i - 1]
        self._items[targetIndex] = item
        self._size += 1
        self.incModCount()

    def pop(self, i=None):
        """前提: 0 <= i < len(self).
        移除并返回索引i位置的值.
        如果i = None, 就给i个默认值len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("list index out of range")
        item = self._items[i]
        for j in range(i, len(self) - 1):
            self._items[j] = self._items[j + 1]
        self._size -= 1
        self.incModCount()
        # 调整数组大小
        self._items.pop()
        return item