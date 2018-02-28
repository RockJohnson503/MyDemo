# encoding: utf-8

"""
File: linkedbag.py
Author: Rock Johnson
"""
from dataStructure.node import Node

class LinkedBag(object):
    """基于linked的bag实现."""

    # 构造函数
    def __init__(self, sourceCollection = None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        self._items = None
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # 进行访问的方法
    def isEmpty(self):
        """当len(self) == 0时返回True,否则返回False."""
        return self._size == 0

    def __len__(self):
        """返回self的长度."""
        return self._size

    def __str__(self):
        """将self以字符串的形式表现."""
        mid = ""
        for i, item in enumerate(self):
            if i == 0:
                if isinstance(item, str):
                    mid += "'" + str(item) + "'"
                else:
                    mid += str(item)
            elif isinstance(item, str):
                mid += "->'" + str(item) + "'"
            else:
                mid += "->" + str(item)
        if mid == "":
            mid = "null"
        return mid

    def __iter__(self):
        """支持将self进行迭代."""
        cursor = self._items
        while cursor != None:
            yield  cursor.data
            cursor = cursor.next

    def __add__(self, other):
        """返回一个包含self以及other的新bag."""
        result = LinkedBag(self)
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

    # 赋值的函数
    def clear(self):
        """使self变为空的."""
        self._size = 0
        self._items = None

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