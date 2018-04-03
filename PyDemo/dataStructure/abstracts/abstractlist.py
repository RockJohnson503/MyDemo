# encoding: utf-8

"""
File: abstractlist.py
Author: Rock Johnson
"""
from dataStructure.funtools.func import tostr
from dataStructure.arrays.arraylistiterator import ArrayListIterator
from dataStructure.abstracts.abstractcollection import AbstractCollection

class AbstractList(AbstractCollection):
    """list数据结构的抽象类实现."""

    def __init__(self, sourceCollection=None):
        self._modCount = 0
        AbstractCollection.__init__(self, sourceCollection)

    # 访问函数
    def __str__(self):
        """返回字符串."""
        return "[" + ", ".join(map(tostr, self)) + "]"

    def getModCount(self):
        """返回self修改的次数."""
        return self._modCount

    def incModCount(self):
        """增加self修改的次数."""
        self._modCount += 1

    def index(self, item, all=False):
        """前提: item在self里面.
        返回item的索引.
        异常: 如果item不在self里面则抛出KeyError异常."""
        if all:
            res = []
        for position, data in enumerate(self):
            if data == item:
                if all:
                    res.append(position)
                else:
                    return position
        if all and res != []:
            return tuple(res)
        raise ValueError(str(item) + " Not in list.")

    # 赋值的函数
    def add(self, item):
        """将item添加到self里面."""
        self.append(item)

    def remove(self, item):
        """前提: item在self里面.
        异常: 如果item不在self里面则抛出KeyError异常.
        后置: 将item从self里移除."""
        position = self.index(item)
        self.pop(position)

    def listIterator(self):
        """返回列表迭代器."""
        return ArrayListIterator(self)