# encoding: utf-8

"""
File: linkedlist.py
Author: Rock Johnson
"""
from dataStructure.linkeds.node import TwoWayNode
from dataStructure.abstracts.abstractlist import AbstractList
from dataStructure.arrays.arraylistiterator import ArrayListIterator

class LinkedList(AbstractList):
    """基于linked的list实现."""

    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        self._head = TwoWayNode(None)
        self._head.previous = self._head.next = self._head.data
        AbstractList.__init__(self, sourceCollection)

    # 访问函数
    def __iter__(self):
        """支持将self进行迭代."""
        cursor = self._head.next
        while cursor != self._head:
            yield cursor.data
            cursor = cursor.next

    # Helper method returns node at position i
    def _getNode(self, i):
        """Helper method: returns a pointer to the node
        at position i."""
        if i == len(self):  # Constant-time access to head node
            return self._head
        if i == len(self) - 1:  # or last data node
            return self._head.previous
        probe = self._head.next
        while i > 0:
            probe = probe.next
            i -= 1
        return probe

    def __getitem__(self, i):
        """前提: 0 <= i < len(self)
        返回索引i的item.
        Raises: IndexError."""
        if isinstance(i, int):
            if i < 0: i += len(self)
            if i < 0 or i >= len(self): raise IndexError("index out of range")
            probe = self._head.next
            for i in range(i):
                probe = probe.next
            return probe.data
        elif isinstance(i, slice):
            start = i.start
            stop = i.stop
            step = i.step
            if step == 0: raise ValueError("slice step cannot be zero")
            if not start: start = 0
            if not stop: stop = 0
            if not step: step = 1
            if start < 0: start += len(self)
            if stop < 0: stop += len(self)
            if start < 0: start = 0
            if stop < 0: stop = 0
            if stop > len(self): stop = len(self)
            if start > len(self): start = len(self)
            probe = self._head.next
            newList = LinkedList()
            if step > 0:
                for i in range(start):
                    probe = probe.next
                for i in range(start, stop, step):
                    newList.append(probe.data)
                    probe = probe.next
            else:
                for i in range(start):
                    probe = probe.next
                for i in range(start, stop, step):
                    probe = probe.previous
                    newList.append(probe.data)
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
            probe = self._head
            while i >= 0:
                probe = probe.next
                i -= 1
            probe.data = value
        elif isinstance(i, slice):
            start = i.start
            stop = i.stop
            step = i.step
            if not start: start = 0
            if not stop: stop = 0
            if not step: step = 0
            if start < 0: start += len(self)
            if stop < 0: stop += len(self)


    def insert(self, i, item):
        """将item插入索引i的位置."""
        if i < 0: i = 0
        elif i > len(self): i = len(self)
        theNode = self._getNode(i)
        newNode = TwoWayNode(item, theNode.previous, theNode.next)
        theNode.next = newNode
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
            raise IndexError("list index of list")
        item = self[i]
        for j in range(i, len(self) - 1):
            self[j] = self[j + 1]
        self._size -= 1
        self.incModCount()
        return item

    def listIterator(self):
        """返回列表迭代器."""
        return ArrayListIterator(self)