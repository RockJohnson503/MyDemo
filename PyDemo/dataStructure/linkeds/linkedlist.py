# encoding: utf-8

"""
File: linkedlist.py
Author: Rock Johnson
"""
from dataStructure.funtools.func import treatSlice
from dataStructure.linkeds.node import TwoWayNode
from dataStructure.abstracts.abstractlist import AbstractList

class LinkedList(AbstractList):
    """基于linked的list实现."""

    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        AbstractList.__init__(self, sourceCollection)

    # 访问函数
    def __iter__(self):
        """支持将self进行迭代."""
        cursor = self._items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node
        at position i."""
        probe = self._items
        for j in range(i):
            probe = probe.next
        return probe

    def __getitem__(self, i):
        """前提: 0 <= i < len(self)
        返回索引i的item.
        Raises: IndexError."""
        if isinstance(i, int):
            if i < 0: i += len(self)
            if i < 0 or i >= len(self): raise IndexError("index out of range")
            probe = self._items
            for i in range(i):
                probe = probe.next
            return probe.data
        elif isinstance(i, slice):
            slices = treatSlice(i, len(self))
            start = slices[0]
            stop = slices[1]
            step = slices[2]
            probe = self._items
            newList = LinkedList()
            for i in range(start):
                probe = probe.next
            for i in range(start - stop):
                if i % abs(step) == 0:
                    newList.append(probe.data)
                if step > 0:
                    probe = probe.next
                else:
                    probe = probe.previous
            return newList


    # 赋值函数
    def __setitem__(self, i, value):
        """前提: 0 <= i < len(self)
        将索引i的值替换成value.
        Raises: IndexError."""
        if isinstance(i, int):
            if i < 0: i += len(self)
            if i < 0 or i >= len(self):
                raise IndexError("list index out of range")
            probe = self._items
            for i in range(i):
                probe = probe.next
            probe.data = value
        elif isinstance(i, slice):
            slices = treatSlice(i, len(self))
            start = slices[0]
            stop = slices[1]
            step = slices[2]
            probe = self._items
            for i in range(start):
                probe = probe.next
            j = 0
            for i in range(start - stop):
                if i % abs(step) == 0:
                    probe.data = value[j]
                    j += 1
                if step > 0:
                    probe = probe.next
                else:
                    probe = probe.previous

    def append(self, item):
        """将item添加到self的末尾."""
        self.insert(len(self), item)

    def insert(self, i, item):
        """将item插入索引i的位置."""
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        if self.isEmpty():
            self._items = TwoWayNode(item)
        elif i == 0:
            self._items = TwoWayNode(item, next=self._items)
            self._items.next.previous = self._items
        elif i == len(self):
            theNode = self._getNode(i - 1)
            newNode = TwoWayNode(item, theNode, None)
            theNode.next = newNode
        else:
            theNode = self._getNode(i)
            newNode = TwoWayNode(item, theNode.previous, theNode)
            theNode.previous.next = newNode
            theNode.previous = newNode
        self._size += 1
        self.incModCount()

    def pop(self, i=None):
        """前提: 0 <= i < len(self).
        移除并返回索引i位置的值.
        如果i = None, 就给i个默认值len(self) - 1.
        Raises: IndexError."""
        if i == None: i = len(self) - 1
        if i < 0 or i >= len(self):
            raise IndexError("list index out of range")
        theNode = self._getNode(i)
        item = theNode.data
        if i == 0:
            self._items = self._items.next
        elif i == len(self) - 1:
            theNode.previous.next = None
        else:
            theNode.next.previous = theNode.previous
            theNode.previous.next = theNode.next
        self._size -= 1
        self.incModCount()
        return item