# encoding: utf-8

"""
File: tuple_testx.py
Author: Rock Johnson
"""
user_list = ["Rock", 18, 177]
name, age, height = user_list
after,  *center, end = name
center = "".join(center)
print(after, center, end)
