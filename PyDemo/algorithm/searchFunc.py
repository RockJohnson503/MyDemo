# encoding: utf-8

"""
File: searchFunc.py
Author: Rock Johnson
"""
class Search:

    def __init__(self):
        self.__index = -1
        self.__isFind = False

    def searchDepth(self, arr, target):
        self.searchHelper(arr, target, 0, len(arr) - 1)
        return self.__index

    def searchHelper(self, arr, target, left, right):
        mid = (left + right) // 2
        if arr[mid] == target:
            self.__index = mid
            self.__isFind = True
        elif not self.__isFind:
            if left <= mid - 1:
                self.searchHelper(arr, target, left, mid - 1)
            if mid + 1 <= right:
                self.searchHelper(arr, target, mid + 1, right)