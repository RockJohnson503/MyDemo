# encoding: utf-8

"""
File: node.py
Author: Rock Johnson
"""
class Node(object):
    """代表单个链表的节点."""

    def __init__(self, data, next = None):
        """实例化一个Node它的next默认值为None."""
        self.data = data
        self.next = next

class TwoWayNode(object):
    """代表双个链表的节点."""

    def __init__(self, data, previous = None, next = None):
        """初始化一个TwoWayNode."""
        Node.__init__(self, data, next)
        self.previous = previous