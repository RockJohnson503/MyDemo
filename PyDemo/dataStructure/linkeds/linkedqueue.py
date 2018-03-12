# encoding: utf-8

"""
File: linkedqueue.py
Author: Rock Johnson
"""
from dataStructure.linkeds.node import Node
from dataStructure.abstracts.abstractqueue import AbstractQueue

class LinkedQueue(AbstractQueue):
    """基于linked的queue实现."""

    # 构造函数
    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        self._rear = None
        self._front = None
        AbstractQueue.__init__(self, sourceCollection)

    # 进行访问的方法
    def __iter__(self):
        """支持将self进行迭代."""
        probe = self._front
        while probe != None:
            yield probe.data
            probe = probe.next

    def peek(self):
        """返回stack的队头项.
        前提: queue不是空的.
        如果是空的则抛出异常."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
        return self._front.data

    # 赋值的函数
    def add(self, item):
        """将item插入queue的队尾."""
        newNode = Node(item, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1

    def pop(self):
        """移除并返回queue的队头项.
        前提: queue不为空.
        Raises: KeyError如果queue为空.
        后置条件: 将队头项从queue中移除."""
        if self.isEmpty():
            raise KeyError("the queue is empty")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem