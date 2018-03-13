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

def treatSlice(slices, length):
    # 处理slice参数
    start = slices.start
    stop = slices.stop
    step = slices.step
    if step == 0: raise ValueError("slice step cannot be zero")
    if not start: start = 0
    if not stop: stop = 0
    if not step: step = 1
    if start < 0: start += length
    if stop < 0: stop += length
    if start < 0: start = 0
    if stop < 0: stop = -1
    if stop > length: stop = length
    if start > length: start = length - 1

    return start, stop, step