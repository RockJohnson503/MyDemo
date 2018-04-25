# encoding: utf-8

"""
File: defaultdict_test.py
Author: Rock Johnson
"""
from collections import defaultdict

dt = defaultdict(int)
dt[1] += 1
print(dt)