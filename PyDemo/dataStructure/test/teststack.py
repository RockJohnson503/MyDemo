# encoding: utf-8

"""
File: teststack.py
Author: Rock Johnson
"""
from dataStructure.linkeds.linkedstack import LinkedStack

def test(stackType):
    # Test any implementation with the same code
    s = stackType()
    print("Length: ", len(s))
    print("Empty: ", s.isEmpty())
    print("Push 1-10")
    for i in range(10):
        s.push(i + 1)
    print("Peeking: ", s.peek())
    print("Items (bottom to top): ", s)
    print("Length: ", len(s))
    print("Empty: ", s.isEmpty())
    theClone = stackType(s)
    print("Items in clone (bottom to top): ", theClone)
    theClone.clear()
    print("Length of clone after clear: ", len(theClone))
    print("Push 11")
    s.push(11)
    print("Popping items (top to bottom): ", end="")
    while not s.isEmpty(): print(s.pop(), end=" ")
    print("\nLength: ", len(s))
    print("Empty: ", s.isEmpty())

if __name__ == '__main__':
    # test(ArrayStack)
    test(LinkedStack)
    pass