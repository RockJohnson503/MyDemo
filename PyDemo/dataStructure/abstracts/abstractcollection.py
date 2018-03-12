# encoding: utf-8

"""
File: abstractcollection.py
Author: Rock Johnson
"""
from dataStructure.arrays.arrays import Array

class AbstractCollection(object):
    """全部数据结构的抽象类实现."""

    # 构造函数
    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        self._type = str(type(self))
        if "Linked" in self._type:
            self._items = None
        elif "Array" in self._type:
            self._items = Array(0)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                if "List" not in self._type:
                    self.add(item)
                else:
                    self.append(item)

    # 进行访问的方法
    def isEmpty(self):
        """当len(self) == 0时返回True,否则返回False."""
        return self._size == 0

    def __len__(self):
        """返回self的长度."""
        return self._size

    def __add__(self, other):
        """返回一个包含self以及other的新数据结构."""
        result = type(self)(self)
        for item in other:
            if "List" not in self._type:
                result.add(item)
            else:
                result.append(item)
        return result

    def __eq__(self, other):
        """当self等于other时返回True,否者返回False."""
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other): return  False
        for item in zip(self, other):
            if item[0] != item[1]: return False
        return True

    def __iter__(self):
        """支持将self进行迭代."""
        cursor = 0
        while cursor < self._size:
            yield self._items[cursor]
            cursor += 1

    # 赋值的函数
    def clone(self):
        """返回一个当前运行对象的完整副本"""
        return type(self)(self)

    def clear(self):
        """使self变为空的."""
        self._size = 0
        if "Linked" in self._type:
            self._items = None
        elif "Array" in self._type:
            self._items = Array(0)