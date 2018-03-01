# encoding: utf-8

"""
File: testbag.py
Author: Rock Johnson
"""
import random
from datetime import datetime
from dataStructure.arraybag import ArrayBag
from dataStructure.linkedbag import LinkedBag
from dataStructure.arraysortedbag import ArraySortedBag

def test(bagType):
    """期望bag类型的对象作为参数并对该类型的对象运行一些测试."""
    # lyst = [random.randrange(10**3) for i in range(10**4)]
    lyst = [2013, 61, 1973]
    print("The list of items added is: ", lyst)
    b1 = bagType(lyst)
    print("Expect 3: ", len(b1))
    print("Expect the bag's string: ", b1)
    print("Expect True: ", 2013 in b1)
    print("Expect False: ", 2012 in b1)
    print("Expect the items on separate lines: ")
    for item in b1:
        print(item)
    b1.clear()
    print("Expect {}: ", b1)
    b1.add(25)
    b1.remove(25)
    print("Expect {}: ", b1)
    b1 = bagType(lyst)
    b2 = bagType(b1)
    print("Expect True: ", b1 == b2)
    print("Expect False: ", b1 is b2)
    print("Expect two of each item: ", b1 + b2)
    for item in lyst:
        b1.remove(item)
    print("Expect {}: ", b1)
    # print("Expect crash with KeyError: ")
    # b2.remove(99)

if __name__ == '__main__':
    star = datetime.now()
    # test(ArrayBag)
    test(LinkedBag)
    # test(ArraySortedBag)
    print(datetime.now() - star)
    pass