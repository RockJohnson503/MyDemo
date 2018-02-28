# encoding: utf-8

"""
File: testnode.py
Author: Rock Johnson
"""
from dataStructure.node import Node

head = None

# 将5个节点添加到链接结构的开头
for count in range(1, 6):
    head = Node(count, head)

# 遍历并打印链表结构的节点
def toStr(linked):
    probe = linked
    while probe != None:
        print(probe.data)
        probe = probe.next

# 搜索链表结构
def search(linked, target):
    probe = linked
    while probe != None and target != probe.data:
        probe = probe.next
    if probe != None:
        print("Found")
    else:
        print("Not found")

# 根据索引搜索链表结构
def searchForIndex(linked, index):
    probe = linked
    if index < 0:
        raise IndexError("index out of the nodes")
    while index > 0:
        probe = probe.next
        index -= 1
    print(probe.data)

# 替换链表结构的节点
def replace(linked, target, new):
    probe = linked
    while probe != None and target != probe.data:
        probe = probe.next
    if probe != None:
        probe.data = new
    else:
        raise KeyError(str(target) + " not in nodes")

# 根据索引替换链表结构的节点
def replaceForIndex(linked, index, new):
    probe = linked
    if index < 0:
        raise IndexError("index out of the nodes")
    while index > 0:
        probe = probe.next
        index -= 1
    probe.data = new

# 在链表结构开始处插入节点
def add(linked, new):
    linked = Node(new, linked)

# 在链表结构末尾插入节点
def append(linked, new):
    newNode = Node(new)
    if linked is None:
        linked = newNode
    else:
        probe = linked
        while probe.next != None:
            probe = probe.next
        probe.next = newNode

# 从末尾处删除节点
def pop(linked):
    probe = linked
    removedNode = probe.data
    probe = probe.next
    return removedNode

if __name__ == '__main__':
    toStr(head)
    print("===================")
    add(head, 10)
    print("===================")
    toStr(head)
    pass