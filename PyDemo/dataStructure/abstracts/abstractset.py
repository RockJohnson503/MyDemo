# encoding: utf-8

"""
File: abstractset.py
Author: Rock Johnson
"""
class AbstractSet(object):
    """set数据结构的抽象类实现."""

    # 访问方法
    def __or__(self, other):
        """返回self和other的并集."""
        return self + other

    def __and__(self, other):
        """返回self和other的交集."""
        intersection = type(self)()
        for item in self:
            if item in other:
                intersection.add(item)
        return intersection

    def __sub__(self, other):
        """返回self和other的差集."""
        difference = type(self)()
        for item in self:
            if item not in other:
                difference.add(item)
        return difference

    def issubset(self, other):
        """如果self是other的子集,返回True,否则返回False."""
        for item in self:
            if item not in other:
                return False
        return True