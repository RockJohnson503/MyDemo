# encoding: utf-8

"""
File: arraysortedbag.py
Author: Rock Johnson
"""
from dataStructure.arraybag import ArrayBag

class ArraySortedBag(ArrayBag):
    """基于array的sorted bag实现."""

    # 构造函数
    def __init__(self, sourceCollection = None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        ArrayBag.__init__(self, sourceCollection)

    # 进行访问的方法
    def __contains__(self, item):
        """如果item在self里面则返回True否则返回False"""
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._items[mid] == item:  return True
            elif self._items[mid] > item: right = mid - 1
            else:                         left = mid + 1
        return False

    # 赋值的函数
    def add(self, item):
        """将item添加进self."""
        # 如果item是最后一个或者self是空的
        # 则直接调用ArrayBag的add方法
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            self._items.add()
            targetIndex = 0
            left = 0
            right = len(self) - 1
            while left <= right:
                mid = (left + right) // 2
                if self._items[mid] <= item and self._items[mid + 1] >= item:
                    targetIndex = mid + 1
                    break
                elif self._items[mid] > item:
                    right = mid - 1
                else:
                    left = mid + 1
            for i in range(len(self._items) - 1, targetIndex, -1):
                self._items[i] = self._items[i - 1]
            self._items[targetIndex] = item
            self._size += 1


    def remove(self, item):
        """前提: item在self里面.
        Raises: KeyError如果item不在self里面.
        后置条件: 将item从self中移除."""
        # 搜索包含目标item的索引
        targetIndex = 0
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._items[mid] == item:
                targetIndex = mid
                break
            elif self._items[mid] > item:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # item没在bag里面的情况
            raise KeyError(str(item) + " not in bag")
        # 将item右边的所有元素向左移动一个位置
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # 递减逻辑大小
        self._size -= 1
        self._items.pop()