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
    def isEmpty(self):
        """当len(self) == 0时返回True,否则返回False."""
        return self._size == 0

    def __len__(self):
        """返回self的长度."""
        return self._size

    def __str__(self):
        """将self以字符串的形式表现."""
        mid = ""
        for i, item in enumerate(self):
            if i == 0:
                if isinstance(item, str):
                    mid += "'" + str(item) + "'"
                else:
                    mid += str(item)
            elif isinstance(item, str):
                mid += ", '" + str(item) + "'"
            else:
                mid += ", " + str(item)
        return "[" + mid + "]"

    def __iter__(self):
        """支持将self进行迭代."""
        cursor = 0
        while cursor < self._size:
            yield  self._items[cursor]
            cursor += 1

    def __add__(self, other):
        """返回一个包含self以及other的新bag."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """当self等于other时返回True,否者返回False."""
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other): return  False
        for item in zip(self, other):
            if item[0] != item[1]: return False
        return True

    def __contains__(self, item):
        """如果item在self里面则返回True否则返回False"""
        left = 0
        right = len(self) - 1
        while left <= right:
            mid = (left + right) // 2
            if self._items[mid] == item:
                return True
            elif self._items[mid] > item:
                right = mid - 1
            else:
                left = mid + 1
        return False

    # 赋值的函数
    def clear(self):
        """使self变为空的."""
        ArrayBag.clear(self)

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
                break0
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
