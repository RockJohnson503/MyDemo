# encoding: utf-8

"""
File: brackets.py
Author: Rock Johnson
"""
from dataStructure.linkeds.linkedstack import LinkedStack

def bracketsBalance(exp):
    """exp is a string that represents the expression"""
    stk = LinkedStack()                 # Create a new stack
    for ch in exp:                      # Scan across the expression
        if ch in ["[", "(", "{"]:       # Push an opening bracket
            stk.push(ch)
        elif ch in ["]", ")", "}"]:     # Process a closing bracket
            if stk.isEmpty():           # Not balanced
                return False
            chFromStack = stk.pop()
            # Brackets must be of same type and match up
            if ch == "]" and chFromStack != "[" or \
                ch == ")" and  chFromStack != "(" or \
                ch == "}" and chFromStack != "{":
                return False
    return stk.isEmpty()                # They all matched up

def main():
    exp = input("请输入括号: ")
    if bracketsBalance(exp):
        print("OK")
    else:
        print("Not OK")

if __name__ == '__main__':
    main()
    pass