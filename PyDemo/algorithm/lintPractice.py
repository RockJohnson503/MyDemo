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


if __name__ == '__main__':
    print(mergeSortedArray2([2,4,5,6, 8], [1,2,3,4, 7]))
    pass