# encoding: utf-8

"""
File: testlist.py
Author: Rock Johnson
"""
from dataStructure.arrays.arraylist import ArrayList

def test(listType):
    print("Create a list with 1-9")
    lst = listType(range(9))
    print("Length: ", len(lst))
    print("Items (first to last): ", lst)

    # Create and use a list iterator
    li = lst.listIterator()
    print("Forward traversal: ", li.first())
    while li.hasNext():
        print(li.next(), end=" ")
    print("\nBackward traversal: ", li.last())
    while li.hasPrevious():
        print(li.previous, end=" ")
    print("\nInserting 10 before 3: ", end="")
    li.first()
    for count in range(2):
        li.next()
    li.insert(10)
    print(lst)
    print("Removing 2: ", end="")
    li.first()
    for count in range(3):
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
    test(ArrayList)
    pass