# encoding: utf-8

"""
File: func.py
Author: Rock Johnson
"""
from functools import wraps

def memo(func):
    # 记忆体化的装饰器函数
    cache = {}                          # 储存子问题的解决方案
    @wraps(func)                        # 使wrap函数看起来像func函数
    def wrap(*args):                    # 内存化的wrap函数
        if args not in cache:           # 检查当前解决方案是否计算过?
            cache[args] = func(*args)   # 计算并缓存解决方案
        return cache[args]              # 返回已缓存的解决方案
    return wrap                         # 返回wrap函数

def tostr(item):
    # 判断item是否为字符串
    if isinstance(item, str):
        return "'" + str(item) + "'"
    else:
        return str(item)