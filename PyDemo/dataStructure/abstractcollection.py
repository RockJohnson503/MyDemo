# encoding: utf-8

"""
File: abstractcollection.py
Author: Rock Johnson
"""
class AbstractCollection(object):
    """全部数据结构的抽象类实现."""

    # 构造函数
    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection: self.add(item)

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
            result.add(item)
        return result

    def __eq__(self, other):
        """当self等于other时返回True,否者返回False."""
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other): return  False
        for item in zip(self, other):
            if item[0] != item[1]: return False
        return True