# encoding: utf-8

"""
File: namedtuple_test.py
Author: Rock Johnson
"""
from collections import namedtuple


name_tuple = (["rock", 17, 177], ["johnson", 18, 188])
User = namedtuple("User", ["name", "age", "height"])
user = []
for name in name_tuple:
    user.append(User(*name))
print(user)