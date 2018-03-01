# encoding: utf-8

"""
File: linkedstack.py
Author: Rock Johnson
"""
from dataStructure.node import Node
from dataStructure.abstractstack import AbstractStack

class LinkedStack(AbstractStack):
    """基于linked的stack实现."""

    # 构造函数
    def __init__(self, sourceCollection = None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractStack.__init__(self, sourceCollection)

    # 进行访问的方法
    def __iter__(self):
        """支持将self进行迭代.
        从stack的底部到顶部访问items."""
        def visitNodes(node):
            if node != None:
                visitNodes(node.next)
                tempList.append(node.data)
        tempList = list()
        visitNodes(self._items)
        return iter(tempList)

    def peek(self):
        """返回stack的顶部元素.
        前提: stack不是空的.
        如果是空的则抛出异常."""
        if self.isEmpty():
            raise KeyError("the stack is empty")
        return self._items.data

    # 赋值的函数
    def push(self, item):
        """将item插入stack的顶部."""
        self._items = Node(item, self._items)
        self._size += 1

    def pop(self):
        """移除并返回stack的顶部元素.
        前提: stack不为空.
        Raises: KeyError如果stack为空.
        后置条件: 将顶部元素从stack中移除."""
        # 搜索包含目标item的索引
        oldItem = self._items.data
        self._items = self._items.next
        self._size -= 1
        return oldItem