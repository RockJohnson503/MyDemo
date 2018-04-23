# encoding: utf-8

"""
File: lintPractice.py
Author: Rock Johnson
"""


# 第K大的数
def kthLargestElement(k, A):
    return quik_sort_helper(A, 0, len(A) - 1, k)


def quik_sort_helper(lst, left, right, k):
    if left <= right:
        pivot = partition(lst, left, right)
        if pivot + 1 == k:
            return lst[pivot]
        elif pivot + 1 > k:
            return quik_sort_helper(lst, left, pivot - 1, k)
        else:
            return quik_sort_helper(lst, pivot + 1, right, k)


def partition(lst, left, right):
    mid = (left + right) // 2
    lst[mid], lst[right] = lst[right], lst[mid]
    boundary = left
    for i in range(left, right):
        if lst[i] > lst[right]:
            lst[i], lst[boundary] = lst[boundary], lst[i]
            boundary += 1
    lst[right], lst[boundary] = lst[boundary], lst[right]
    return boundary


# 合并排序数组2
def mergeSortedArray1(A, B):
    for i in range(len(B)):
        if A[-1] <= B[0]:
            A.append(B.pop(0))
        elif A[0] >= B[0]:
            A.insert(0, B.pop(0))
        else:
            left = 0
            right = len(A) - 1
            while left <= right:
                mid = (left + right) // 2
                if A[mid] == B[0] or (A[mid] < B[0] and A[mid + 1] > B[0]):
                    A.insert(mid + 1, B.pop(0))
                    break
                elif A[mid] > B[0]:
                    right = mid - 1
                else:
                    left = mid + 1
    return A

def mergeSortedArray2(A, B):
    new_lst = []
    A_point = 0
    B_point = 0
    while A_point < len(A) or B_point < len(B):
        if A_point == len(A):
            new_lst.append(B[B_point])
            B_point += 1
        elif B_point == len(B):
            new_lst.append(A[A_point])
            A_point += 1
        elif A[A_point] <= B[B_point]:
            new_lst.append(A[A_point])
            A_point += 1
        else:
            new_lst.append(B[B_point])
            B_point += 1
    return new_lst


# 中位数
def median(nums):
    mid = len(nums) // 2 if len(nums) % 2 != 0 else len(nums) // 2 - 1
    return median_helper(nums, 0, mid, len(nums) - 1)

def median_helper(nums, low, mid, height):
    if low <= height:
        pivot = partition2(nums, low, height)
        if pivot == mid:
            return nums[mid]
        elif pivot < mid:
            return median_helper(nums, pivot + 1, mid, height)
        else:
            return median_helper(nums, low, mid, pivot - 1)

def partition2(nums, low, height):
    mid = (low + height) // 2
    nums[mid], nums[height] = nums[height], nums[mid]
    boundary = low
    for index in range(low, height):
        if nums[index] < nums[height]:
            nums[index], nums[boundary] = nums[boundary], nums[index]
            boundary += 1
    nums[height], nums[boundary] = nums[boundary], nums[height]
    return boundary


if __name__ == '__main__':
    print(median([4]))
    pass