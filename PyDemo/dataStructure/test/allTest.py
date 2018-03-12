# encoding: utf-8

"""
File: allTest.py
Author: Rock Johnson
"""
import random
from dataStructure.wrapper.comparable import Comparable
from dataStructure.arrays.arraybag import ArrayBag
from dataStructure.arrays.arraystack import ArrayStack
from dataStructure.arrays.arrayqueue import ArrayQueue
from dataStructure.arrays.arraylist import ArrayList
from dataStructure.linkeds.linkedbag import LinkedBag
from dataStructure.linkeds.linkedstack import LinkedStack
from dataStructure.linkeds.linkedqueue import LinkedQueue
from dataStructure.arrays.arraysortedbag import ArraySortedBag
from dataStructure.linkeds.linkedpriorityqueue import LinkedPriorityQueue

if __name__ == '__main__':
    # dt = [1]
    # arr = ArrayBag(['1', 1, 2])
    # print(arr)
    # lst = list(dt)
    # print(lst)
    # lin = LinkedBag([i for i in range(10**5)])
    # print(lin)
    # star = datetime.datetime.now()
    # print(lin + [i for i in range(10**5)])
    # print(datetime.datetime.now() - star)
    # arr = LinkedBag([1, 5])
    # arr2 = ArrayBag([1, 1, 3, 2])
    # arr3 = ArraySortedBag([1, 2 ,3])
    # arr3.remove(2)
    # print(arr3)
    # arr2 = arr.clone()
    # print(arr is arr2)
    # lst = [1, 2, 3]
    # lst.clear()
    # print(lst)
    # arr = ArrayQueue()
    # print(arr)
    # arr.add("a")
    # print(arr)
    # arr.add("b")
    # print(arr)
    # arr.add("c")
    # print(arr)
    # print(arr.isEmpty())
    # print(len(arr))
    # print(arr.peek())
    # print(arr.pop())
    # print(arr)
    # print(arr.pop())
    # print(arr)
    # print(arr.pop())
    # print(arr)
    # print(arr.isEmpty())
    # print(arr.peek())
    # print(arr.pop())
    # arr.add("d")
    # print(arr)
    # q = LinkedPriorityQueue([Comparable(i, random.randrange(100)) for i in range(10**4)])
    # print(q)
    ls = [1, 2, 3, 4]
    ls.insert(5, 0)
    print(ls)
    l = ArrayList([1, 2, 3])
    print(l)
    l[2] = 4
    print(l)
    pass