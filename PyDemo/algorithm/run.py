# encoding: utf-8

"""
File: run.py
Author: Rock Johnson
"""
import math
import timeit
import cProfile
import random
import datetime
# import numpy as np
from algorithm.profiler import Profiler
from algorithm.searchFunc import Search
from bisect import *

# 算法习题
def rotateString(strs, offset):
    if offset == 0: return strs
    elif offset > len(strs): offset %= len(strs)

    strs = strs[-offset:] + strs[:len(strs) - offset]
    return strs

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalWeight) + 1, dtype=np.int32)
    for i in range(1, totalLength+1):
        for j in range(totalWeight, 0, -1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j], resArr[j-wlist[i]]+vlist[i])
    return resArr[-1]

def maxSum(triangle):
    if triangle is None or len(triangle) == 0:
        return 0
    tmp = triangle[-1]
    for i in range(len(triangle) - 1, -1, -1):
        if i + 1 < len(triangle):
            for j in range(len(triangle[i])):
                tmp[j] = max(tmp[j], tmp[j + 1]) + triangle[i][j]
    return tmp[0]

def wiggle_sort(lyst):
    lyst.sort()
    i = 1
    while i <= len(lyst):
        lyst.insert(i, lyst.pop())
        i += 2

def searchMatrix(matrix, target):
    left = 0
    right = len(matrix) - 1
    while left <= right:
        midPoint = (left + right) // 2
        if target >= min(matrix[midPoint]) and target <= max(matrix[midPoint]):
            if target in matrix[midPoint]:
                return True
            else:
                return False
        elif target < min(matrix[midPoint]):
            right = midPoint - 1
        elif target > max(matrix[midPoint]):
            left = midPoint + 1
    return False

def maxSlidingWindow(nums, k):
    if nums == []:
        return nums
    left = 0
    right = left + k
    res = []
    while right <= len(nums):
        res.append(max(nums[left: right]))
        left += 1
        right = left + k
    return res

def backPack(m, A):
    dp = [0 for x in range(m + 1)]
    dp[0] = 1
    ans = 0
    for item in A:
        for i in range(m, -1, -1):
            if i - item >= 0 and dp[i - item] > 0:
                ans = max(ans, i)
                dp[i] = 1
    return ans

def demo():
    star = datetime.datetime.now()
    count = 10 ** 6
    nums = []
    for i in range(count):
        # nums.insert(0, i)
        nums.append(i)
    nums.reverse()
    print(datetime.datetime.now() - star)

def desearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] == target or nums[right] == target:
            return True
        else:
            left += 1
            right -= 1
    return False

def binsearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            return target
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return False

def comsearch(nums, target):
    for i in nums:
        if i == target:
            return True
    return False


def game():
    p = random.randrange(100)
    count = 0
    while True:
        count += 1
        try:
            inp = int(input("请输入数字: "))
        except Exception as e:
            print("请输入数字,此次游戏不算,重新计数")
            count = 0
            p = random.randrange(100)
            continue
        if inp == p:
            print("恭喜您猜对了, 总共用了: " + str(count) + "次")
            break
        elif inp > p:
            print("您输入的数大了")
        else:
            print("您输入的数小了")

def minAbsNum(nums):
    nums.sort()
    dif = float("inf")
    resx = 0
    resy = 0
    for i in range(len(nums) - 1):
        x, y = nums[i], nums[i + 1]
        if x == y: continue
        d = abs(x - y)
        if d < dif: resx, resy, dif = x, y, d
    return resx, resy, dif

def medianSlidingWindow(nums, k):
    if nums == [] or k == 1:
        return nums
    left = 0
    lst = []
    res = []
    while True:
        right = left + k
        if right > len(nums):
            break
        lst.append(nums[left:right])
        left += 1
    if k % 2 != 0:
        k //= 2
    else:
        k = k // 2 - 1
    for i in lst:
        res.append(i[k])
    return res

def reversePairs(lyst):
    count = 0
    for i, k in enumerate(lyst):
        for j in lyst[i+1:len(lyst)]:
            if k > j:
                count += 1
    return count

def intersection(nums1, nums2):
    res = []
    nums1 = list(set(nums1))
    nums2 = list(set(nums2))
    if len(nums1) > len(nums2):
        temp = nums1
        nums1 = nums2
        nums2 = temp
    nums2.sort()
    for i in nums1:
        if i in res:
            continue
        sr = binsearch(nums2, i)
        if sr:
            res.append(sr)
    return res

def index(a, x):
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return None

def kthPrime(n):
    count = 0
    if not is_prime(n):
        count = 1
    for i in range(2, n + 1):
        if is_prime(i):
            count += 1
    return count

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fac(n):
    if n == 1:
        return 1
    return fac(n - 1) * n

def land(a, b):
    while a != 0:
        a, b = b % a, a
    return b

def sumDepth(arr):
    if len(arr) == 1:
        return arr[0]
    return arr[0] + sumDepth(arr[1:])


def findMoney(owed):
    denom = {10000: 10, 5000: 10, 2000: 10, 1000: 10, 500: 10, 200: 10, 100: 10, 50: 10, 25: 10, 10: 10, 1: 10}
    payed = {}
    for d in denom.keys():
        while owed >= d:
            if denom[d] == 0:
                break
            owed -= d
            denom[d] -= 1
            if payed.get(d) == None:
                payed[d] = 0
            payed[d] += 1
    if owed == 0:
        return payed
    else:
        return "零钱不够了!"


if __name__ == '__main__':
    # print(findMoney(15216))
    # print(algComp(countingSort, quickSortDepth, mergeSort, bubbleSortWithTweak, selectionSort, bubbleSort, insertSort, num=3))
    # print(sumDepth([2, 4, 6]))
    # lst = [i for i in range(10 ** 4)]
    # print(runTime(quickSortDepth, 4))
    # print(runTime(mySort, 4))
    # print(runTime(quickSortDepth, 4))
    # print(lst)
    # star = datetime.datetime.now()
    # search = Search()
    # print(search.searchDepth(lst, 10**5 - 1))
    # print(comsearch(lst, 10**5 - 1))
    # print(datetime.datetime.now() - star)
    # lst = [random.randrange(10**10) for i in range(10**5)]
    # start = datetime.datetime.now()
    # medianSlidingWindow(lst, 100)
    # print(datetime.datetime.now() - start)
    # lst1 = [i for i in range(10**4)]
    # lst2 = [i for i in range(10**4)]
    # start = datetime.datetime.now()
    # selectionSort(lst)
    # bubbleSort(lst)
    # bubbleSortWithTweak(lst)
    # insertSort(lst)
    # quickSortDepth(lst)
    # mergeSort(lst)
    # countingSort(lst)
    # mySort(lst)
    # sorted(lst)
    # lst.sort()
    # intersection(lst1, lst2)
    # print(datetime.datetime.now() - start)
    # print(isSort(lst))
    # lst2 = [5, 4, 2, 1, 3]
    # mergeSort(lst2)
    # print(lst2)
    # lst = [2,4,1,3,5]
    # start = datetime.datetime.now()
    # print(index(lst, 1))
    # lst.index(10**5-1)
    # print(kthPrime(10**5))
    # print(datetime.datetime.now() - start)
    # p = Profiler()
    # p.test(selectionSort, size=10**4)
    # lst = [i for i in range(10, 0, -1)]
    # print(lst)
    # print(isSort(lst))
    # quickSort(lst)
    # print(lst)
    # start = datetime.datetime.now()
    # print(isSort(lst))
    # print(datetime.datetime.now() - start)
    pass
