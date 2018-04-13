# encoding: utf-8

"""
File: sorts.py
Author: Rock Johnson
"""
import math
import random
import datetime
from collections import defaultdict
from dataStructure.arrays.arrays import Array


# ----------------测试区-------------------
def is_sort(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

def compare(*args, num=3, size=100):
    for item in args:
        if type(item) != type(compare):
            raise TypeError("error parameter, parameter must be functions")
    dic = {}
    for fun in args:
        dic[fun.__name__] = float(run_time(fun, num, size)[:-2])
    sortedTime = sorted(dic.values())
    sortedFun = []
    for i in sortedTime:
        sortedFun += [k for k,v in dic.items() if v == i]
    return " <- ".join(sortedFun)

def run_time(fun, num=3, size=100):
    timeSum = 0
    for i in range(size):
        lst = [random.randrange(100) for i in range(10 ** num)]
        start = datetime.datetime.now()
        res = fun(lst)
        timeSum += (datetime.datetime.now() - start).microseconds
        flag = is_sort(res) if res != None else is_sort(lst)
        if not flag:
            raise SyntaxError("your sort ALG is wrong!")
    return str(timeSum / size) + "ms"


# ----------------算法区-------------------
# 乱写的排序
def my_sort(lst):
    newLst = []
    for i in lst:
        my_add(newLst, i)
    for i in range(len(lst)):
        lst[i] = newLst[i]

def my_add(lst, item):
    if len(lst) == 0 or item >= lst[-1]:
        lst.append(item)
    elif item <= lst[0]:
        lst.insert(0, item)
    else:
        left = 0
        right = len(lst) - 1
        index = 0
        while left <= right:
            mid = (left + right) // 2
            if item >= lst[mid] and item <= lst[mid + 1]:
                index = mid + 1
                break
            elif item > lst[mid]:
                left = mid + 1
            else:
                right = mid - 1
        lst.insert(index, item)


# 选择排序
def selection_sort(lst):
    for i in range(len(lst) - 1):
        minIndex = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]


# 冒泡排序
def bubble_sort(lst):
    for i in range(len(lst), 0, -1):
        for j in range(1, i):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]


# 改良后的冒泡排序
def bubble_sort_tweak(lst):
    for i in range(len(lst), 0, -1):
        swapped = False
        for j in range(1, i):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                swapped = True
        if not swapped: break


# 插入排序
def insert_sort(lst):
    for i in range(1, len(lst)):
        itemToInsert = lst[i]
        newIndex = i
        for j in range(i - 1, -1, -1):
            if itemToInsert < lst[j]:
                lst[j + 1] = lst[j]
                newIndex = j
            else:
                break
        lst[newIndex] = itemToInsert


# 快速排序
# 递归版 1.0
def quick_sort_1(lst):
    quick_sort_helper(lst, 0, len(lst) - 1)

def quick_sort_helper(lst, left, right):
    # 快排的辅助函数
    if left < right:
        pivot = partition(lst, left, right)
        quick_sort_helper(lst, left, pivot - 1)
        quick_sort_helper(lst, pivot + 1, right)

def partition(lst, left, right):
    # 快排实现过程
    # 找到基准点并与最后一项进行交换
    mid = (left + right) // 2
    lst[mid], lst[right] = lst[right], lst[mid]
    # 将边界点设置为第一个位置
    boundary = left
    # 移动items到左侧
    for index in range(left, right):
        if lst[index] < lst[right]:
            lst[index], lst[boundary] = lst[boundary], lst[index]
            boundary += 1
    # 交换基准点和边界
    lst[right], lst[boundary] = lst[boundary], lst[right]
    return boundary


# 精简递归版 2.0
def quick_sort_2(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    return quick_sort_2([x for x in lst[1:] if x < pivot]) + [pivot] + quick_sort_2([x for x in lst[1:] if x >= pivot])


# 一行语法糖版
quick_sort_3 = lambda lst : ( (len(lst) <= 1 and [lst]) or [ quick_sort_3( [x for x in lst[1:] if x < lst[0]] ) + [lst[0]] + quick_sort_3( [x for x in lst[1:] if x >= lst[0]] ) ] )[0]


# 合并排序
def merge_sort(lst):
    copyBuffer = Array(len(lst))
    merge_sort_helper(lst, copyBuffer, 0, len(lst) - 1)

def merge_sort_helper(lst, copyBuffer, low, high):
    # 合并排序的辅助函数
    if low < high:
        middle = (low + high) // 2
        merge_sort_helper(lst, copyBuffer, low, middle)
        merge_sort_helper(lst, copyBuffer, middle + 1, high)
        merge(lst, copyBuffer, low, middle, high)

def merge(lst, copyBuffer, low, middle, high):
    # 合并排序的实现过程
    # 初始化i1,i2到每个子列表的第一项
    i1 = low
    i2 = middle + 1
    # 将子列表中的项初始化为copyBuffer,以保持顺序
    for i in range(low, high + 1):
        if i1 > middle:
            copyBuffer[i] = lst[i2]
            i2 += 1
        elif i2 > high:
            copyBuffer[i] = lst[i1]
            i1 += 1
        elif lst[i1] < lst[i2]:
            copyBuffer[i] = lst[i1]
            i1 += 1
        else:
            copyBuffer[i] = lst[i2]
            i2 += 1
    for i in range(low, high + 1):
        lst[i] = copyBuffer[i]

# 计数排序
def counting_sort(lst):
    if is_sort(lst):
        return
    dt = defaultdict(list)
    for i in lst:
        dt[i].append(i)
    lst.clear()
    for i in range(min(dt), max(dt) + 1):
        if i in dt:
            lst.extend(dt[i])


# 希尔排序
def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2


# 堆排序 1.0
def heap_sort_1(lst):
    size = len(lst)
    build_heap(lst, size)
    for i in range(0, size)[::-1]:
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i)

def adjust_heap(lst, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max_num = i
    if i < size / 2:
        if lchild < size and lst[lchild] > lst[max_num]:
            max_num = lchild
        if rchild < size and lst[rchild] > lst[max_num]:
            max_num = rchild
        if max_num != i:
            lst[max_num], lst[i] = lst[i], lst[max_num]
            adjust_heap(lst, max_num, size)

def build_heap(lst, size):
    for i in range(0, int(size / 2))[::-1]:
        adjust_heap(lst, i, size)


# 堆排序 2.0
def heap_sort_2(lst):
    # 创建最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(lst, start, len(lst) - 1)

    # 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(lst, 0, end - 1)

def sift_down(lst, start, end):
    # 最大堆调整
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break


# 基数排序(桶子法)
def radix_sort(lst, radix=100):
    k = math.ceil(math.log(max(lst), radix))
    bucket = [[] for i in range(radix)]
    for i in range(1, k + 1):
        for j in lst:
            bucket[int(j / (radix ** (i - 1)) % (radix ** i))].append(j)
        del lst[:]
        for z in bucket:
            lst += z
            del z[:]


if __name__ == '__main__':
    # print(compare(quick_sort_1, merge_sort, heap_sort_2, radix_sort, counting_sort, shell_sort, num=4))
    # print(run_time(radix_sort, 4))
    # print(run_time(counting_sort, 4))
    pass