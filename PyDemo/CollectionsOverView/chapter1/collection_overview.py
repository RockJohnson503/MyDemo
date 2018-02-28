# encoding: utf-8

"""
File: collection_overview.py
Author: Rock Johnson
"""
from collections import *
from collections.abc import *

c = Counter("")
strs = [1,2,2,3,4,4,5,3]
dt = dict()
for i in strs:
    if dt.get(i) == None:
        dt[i] = 0
    dt[i] += 1

def get_keys(d, value):
    return [k for k,v in d.items() if v == value]

print(dt)
