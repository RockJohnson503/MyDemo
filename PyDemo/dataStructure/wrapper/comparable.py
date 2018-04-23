# encoding: utf-8

"""
File: comparable.py
Author: Rock Johnson
"""
class Comparable(object):
    """用于不可比较的items的包装类."""

    def __init__(self, data, priority = 1):
        self._data  = data
        self._priority = priority

    def __str__(self):
        """返回包含数据的字符串."""
        return str(self._data)

    def __eq__(self, other):
        """如果priority相等则返回True, 否则返回False."""
        if self is other: return True
        if type(self) != type(self): return False
        return self._priority == other._priority

    def __lt__(self, other):
        """如果self的priority小于other的priority返回True, 否则返回False."""
        return self._priority < other._priority

    def __le__(self, other):
        """如果self的priority小于或等于other的priority返回True, 否则返回False."""
        return self._priority <= other._priority

    def getData(self):
        """返回数据."""
        return self._data

    def getPriority(self):
        """返回优先级."""
        return self._priority