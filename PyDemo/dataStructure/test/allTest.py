# encoding: utf-8

"""
File: allTest.py
Author: Rock Johnson
"""
import datetime
from dataStructure.arraybag import ArrayBag
from dataStructure.linkedbag import LinkedBag
from dataStructure.arraysortedbag import ArraySortedBag

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
    arr = LinkedBag([1, 5])
    # arr2 = ArrayBag([1, 1, 3, 2])
    # arr3 = ArraySortedBag([1, 2 ,3])
    # arr3.remove(2)
    # print(arr3)
    arr.clear()
    print(type(arr))
    pass