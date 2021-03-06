# encoding: utf-8

"""
File: testlist.py
Author: Rock Johnson
"""
import datetime, random
from dataStructure.arrays.arraylist import ArrayList
from dataStructure.linkeds.linkedlist import LinkedList
from dataStructure.arrays.arraysortedlist import ArraySortedList


def test(listType):
    print("Create a list with 1-9")
    lst = listType(range(1, 10))
    print("Length: ", len(lst))
    print("Items (first to last): ", lst)

    # Create and use a list iterator
    li = lst.listIterator()
    print("Forward traversal: ", end="")
    li.first()
    while li.hasNext():
        print(li.next(), end=" ")
    print("\nBackward traversal: ", end="")
    li.last()
    while li.hasPrevious():
        print(li.previous(), end=" ")
    print("\nInserting 10 before 3: ", end="")
    li.first()
    for count in range(3):
        li.next()
    li.insert(10)
    print(lst)
    print("Removing 2: ", end="")
    li.first()
    for count in range(2):
        li.next()
    li.remove()
    print(lst)
    print("Removing all items")
    li.first()
    while li.hasNext():
        li.next()
        li.remove()
    print("Length: ", len(lst))

if __name__ == '__main__':
    star = datetime.datetime.now()
    # test(ArrayList)
    # test(LinkedList)
    test(ArraySortedList)
    print(datetime.datetime.now() - star)
    pass