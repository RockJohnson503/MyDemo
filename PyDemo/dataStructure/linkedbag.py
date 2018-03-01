# encoding: utf-8

"""
File: linkedbag.py
Author: Rock Johnson
"""
from dataStructure.node import Node
from dataStructure.abstractbag import AbstractBag

class LinkedBag(AbstractBag):
    """基于linked的bag实现."""

    # 构造函数
    def __init__(self, sourceCollection = None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractBag.__init__(self, sourceCollection)

    # 进行访问的方法
    def __iter__(self):
        """支持将self进行迭代."""
        cursor = self._items
        while cursor != None:
            yield  cursor.data
            cursor = cursor.next

    # 赋值的函数
    def add(self, item):
        """将item添加进self."""
        self._items = Node(item, self._items)
        self._size += 1

    def remove(self, item):
        """前提: item在self里面.
        Raises: KeyError如果item不在self里面.
        后置条件: 将item从self中移除."""
        # 搜索包含目标item的节点
        # probe将指向目标节点
        # 并且trailer将指向probe之前的那个节点(如果probe存在)
        probe = self._items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
            trailer = probe
            probe = probe.next
        else:
            # item没在bag里面的情况
            raise KeyError(str(item) + " not in bag")
        # 解除要删除的节点,无论是第一个还是之后的节点
        if probe == self._items:
            self._items = self._items.next
        else:
            trailer.next = probe.next
        # 递减逻辑大小
        self._size -= 1

    def clone(self):
        """返回一个当前运行对象的完整副本"""
        return LinkedBag(LinkedBag(self))