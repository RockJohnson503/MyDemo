# encoding: utf-8

"""
File: allTest.py
Author: Rock Johnson
"""
from dataStructure.arrays.arraybag import ArrayBag
from dataStructure.arrays.arraystack import ArrayStack
from dataStructure.arrays.arrayqueue import ArrayQueue
from dataStructure.linkeds.linkedbag import LinkedBag
from dataStructure.linkeds.linkedstack import LinkedStack
from dataStructure.linkeds.linkedqueue import LinkedQueue
from dataStructure.arrays.arraysortedbag import ArraySortedBag

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
    arr = LinkedStack()
    print(arr)
    arr.push("a")
    print(arr)
    arr.push("b")
    print(arr)
    arr.push("c")
    print(arr)
    print(arr.isEmpty())
    print(len(arr))
    print(arr.peek())
    print(arr.pop())
    print(arr)
    print(arr.pop())
    print(arr)
    print(arr.pop())
    print(arr)
    print(arr.isEmpty())
    # print(arr.peek())
    # print(arr.pop())
    arr.add("d")
    print(arr)
    pass