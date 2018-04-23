# encoding: utf-8

"""
File: arrays.py
Author: Rock Johnson
"""
class Array(object):
    """表示数组."""

    def __init__(self, capacity, fillValue = None):
        """Capacity是一个静态大小的数组.
        fillValue是放置的每个位置"""
        self._items = list()
        for count in range(capacity): self._items.append(fillValue)

    def __len__(self):
        """返回数组的容量"""
        return len(self._items)

    def __str__(self):
        """以字符串的形式表示该数组"""
        return str(self._items)

    def __iter__(self):
        """支持for循环遍历"""
        return iter(self._items)

    def __getitem__(self, i):
        """下标用于索引访问"""
        return self._items[i]

    def __setitem__(self, key, value):
        """下标在索引出进行替换"""
        self._items[key] = value

    def add(self):
        """增加数组逻辑大小"""
        self._items.append(None)

    def pop(self):
        """减少数组逻辑大小"""
        self._items.pop()