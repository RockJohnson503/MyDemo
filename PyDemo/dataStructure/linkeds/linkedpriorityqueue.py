# encoding: utf-8

"""
File: linkedpriorityqueue.py
Author: Rock Johnson
"""
from dataStructure.linkeds.node import Node
from dataStructure.linkeds.linkedqueue import LinkedQueue

class LinkedPriorityQueue(LinkedQueue):
    """基于linked的优先队列实现."""

    def __init__(self, sourceCollection=None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        LinkedQueue.__init__(self, sourceCollection)

    # 赋值的函数
    def add(self, item):
        """将item插入大于或等于优先级的items之后或者插入优先级较低的item之前.
        如果A < B,则A优先于B."""
        if self.isEmpty() or item >= self._rear.data:
            # 将item插入队尾
            LinkedQueue.add(self, item)
        else:
            # 搜索比item优先级更低的item的位置
            probe = self._front
            while item >= probe.data:
                trailer = probe
                probe = probe.next
            newNode = Node(item, probe)
            if probe == self._front:
                # 将item插入队头
                self._front = newNode
            else:
                # 将item插入两个节点之间
                trailer.next = newNode
            self._size += 1
