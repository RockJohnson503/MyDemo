# encoding: utf-8

"""
File: demo.py
Author: Rock Johnson
"""
from datetime import datetime
from collections import defaultdict
from random import randrange
from itertools import combinations
from functools import wraps

def naive_max_perm(M, A=None):
    # 最大排列
    if A is None:
        A = set(range(len(M)))
    if len(A) == 1: return A
    B = set(M[i] for i in A)
    C = A - B
    if C:
        A.remove(C.pop())
        return naive_max_perm(M, A)
    return A

def max_perm(M):
    n = len(M)
    A = set(range(n))
    count = [0] * n
    for i in M:
        count[i] += 1
    Q = [i for i in A if count[i] == 0]
    while Q:
        i = Q.pop()
        A.remove(i)
        j = M[i]
        count[j] -= 1
        if count[j] == 0:
            Q.append(j)
    return A

def countingSort(A, key=lambda x: x):
    # 计数排序
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C) + 1):
        if k in C:
            B.extend(C[k])
    return B

def naive_celeb(G):
    # 明星问题
    n = len(G)
    for i in range(n):
        for j in range(n):
            if i == j: continue
            if G[i][j]: break
            if not G[j][i]: break
        else:
            return i
    return None

def celeb(G):
    n = len(G)
    i, j = 0, 1
    for c in range(2, n+1):
        if G[i][j]: i = c
        else:       j = c
    if i == n:      c = j
    else:           c = i
    for v in range(n):
        if c == v: continue
        if G[c][v]: break
        if not G[v][c]: break
    else:
        return c
    return None

def naive_topSort(G, S=None):
    # 拓扑排序
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()
    seq = naive_topSort(G, S)
    min_i = 0
    for i, u in enumerate(seq):
        if v in G[u]: min_i = i + 1
    seq.insert(min_i, v)
    return seq

def topSort(G):
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    Q = [u for u in G if count[u] == 0]
    S = []
    while Q:
        u = Q.pop()
        S.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                Q.append(v)
    return S

def naive_lis(seq):
    # 最长递增子序列
    for l in range(len(seq), 0, -1):
        for s in combinations(seq, l):
            if list(s) == sorted(s):
                return s

def memo(func):
    # 记忆体化的装饰器函数
    cache = {}                          # 储存子问题的解决方案
    @wraps(func)                        # 使wrap函数看起来像func函数
    def wrap(*args):                    # 内存化的wrap函数
        if args not in cache:           # 检查当前解决方案是否计算过?
            cache[args] = func(*args)   # 计算并缓存解决方案
        return cache[args]              # 返回已缓存的解决方案
    return wrap                         # 返回wrap函数

@memo
def fib(i):
    # 斐波那契数列
    if i < 2: return 1
    return fib(i - 1) + fib(i - 2)

# @memo
def two_pow(i):
    if i == 0: return 1
    return 2 * two_pow(i - 1)

@memo
def C(n, k):
    if k == 0: return 1
    if n == 0: return 0
    return C(n - 1, k - 1) + C(n - 1, k)

def rec_dag_sp(W, s, t):                            # 从s到t的最短路径
    @memo                                           # 记忆函数
    def d(u):                                       # 从u到t的距离
        if u == t: return 0                         # 如果在那里!
        return min(W[u][v] + d(v) for v in W[u])    # 每个第一步都是最好的
    return d(s)                                     # 将d()应用到实际的起始节点

def dag_sp(W, s, t):
    d = {u:float('inf') for u in W}
    d[s] = 0
    for u in topSort(W):
        if u == t: break
        for v in W[u]:
            d[v] = min(d[v], d[u] + W[u][v])
    return d[t]

@memo
def C(n, k):
    if n == 0 or k == 0 or n == k:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)

# 欧几里得算法-分配最大正方形土地
def devil_land(width, height):
    if width % height == 0 or height % width == 0:
        return height if height < width else width
    longest = divmod(width, height)[1] if width > height else divmod(height, width)[1]
    return devil_land(longest if width > height else (width - longest), (height - longest) if width > height else longest)

def sum_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    elif len(lst) > 1:
        return lst[0] + sum_recursive(lst[1:])

def count_recursive(lst):
    if lst == []:
        return 0
    return 1 + count_recursive(lst[1:])

def max_recursive(lst):
    if len(lst) > 1:
        max_num = max_recursive(lst[1:])
        return lst[0] if lst[0] > max_num else max_num
    elif len(lst) == 1:
        return lst[0]

def binary_recursive(lst, item, low=None, hight=None):
    low = low if low else 0
    hight = hight if hight else len(lst) - 1
    if low >= hight:
        return None
    mid = (low + hight) // 2
    if lst[mid] == item:
        return mid
    elif lst[mid] > item:
        return binary_recursive(lst, item, low, mid - 1)
    else:
        return binary_recursive(lst, item, mid + 1, hight)

if __name__ == '__main__':
    print(binary_recursive([i for i in range(100)], 50))
    # print(fib(39))
    # print(dag_sp({"a": {"b": 2, "f": 9}, "b": {"d": 2, "c": 1, "f": 6}, "c": {"d": 7}, "d": {"e": 2, "f": 3}, "e": {"f": 4}, "f": {}}, "b", "c"))
    # M = [2, 2, 10, 5, 3, 5, 7, 4]
    # print(countingSort(M))
    #
    # n = 10**3
    # G = [[randrange(2) for i in range(n)] for i in range(n)]
    # c = randrange(n)
    # for i in range(n):
    #     G[i][c] = True
    #     G[c][i] = False
    # naive_celeb(G)
    # celeb(G)
    #
    # print(naive_lis([3, 1, 0, 2, 4]))
    #
    # fib = memo(fib)
    # print(fib(5))
    #
    # print(two_pow(100))
    #
    # print(C(6, 1))
    #
    # print(rec_dag_sp(['a', 'b', 'c', 'd'], 'a', 'd'))
    # for i in combinations([1, 2, 3, 2], 3):
    #     print(i)
    pass