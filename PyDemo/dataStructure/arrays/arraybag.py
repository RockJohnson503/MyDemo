# encoding: utf-8

"""
File: arraybag.py
Author: Rock Johnson
"""
from dataStructure.abstracts.abstractbag import AbstractBag

class ArrayBag(AbstractBag):
    """基于array的bag实现."""

    # 构造函数
    def __init__(self, sourceCollection = None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractBag.__init__(self, sourceCollection)

    # 赋值的函数
    def add(self, item):
        """将item添加进self."""
        self._items.add()
        self._items[len(self)] = item
        self._size += 1

    def remove(self, item):
        """前提: item在self里面.
        Raises: KeyError如果item不在self里面.
        后置条件: 将item从self中移除."""
        # 搜索包含目标item的索引
        targetIndex = 0
        for i, targetItem in enumerate(self):
            if targetItem == item:
                targetIndex = i
                break
        else:
            # item没在bag里面的情况
            raise KeyError(str(item) + " not in bag")
        # 将item右边的所有元素向左移动一个位置
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # 递减逻辑大小
        self._size -= 1
        self._items.pop()