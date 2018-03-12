# encoding: utf-8

"""
File: arraylistiterator.py
Author: Rock Johnson
"""
class ArrayListIterator(object):
    """表示arraylist的列表迭代器."""

    def __init__(self, backingStore):
        """设置列表迭代器的初始化状态."""
        self._backingStore = backingStore
        self._modCount = backingStore.getModCount()
        self.first()

    def first(self):
        """将cursor重置到backingStore的开始位置."""
        self._cursor = 0
        self._lastItemPos = -1

    def last(self):
        """移动cursor到backingStore的末尾."""
        self._cursor = len(self._backingStore)
        self._lastItemPos = -1

    def hasNext(self):
        """如果列表迭代器还有下一个item则返回True,否则返回False."""
        return self._cursor < len(self._backingStore)

    def next(self):
        """前提: hasNext()返回True.
        除了迭代器的mutators外,这个列表还没有被修改过.
        返回当前item并移动cursor到下一个item."""
        if not self.hasNext():
            raise ValueError("no next item in list iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("illegal modification of backing store")
        self._lastItemPos = self._cursor
        self._cursor += 1
        return self._backingStore[self._lastItemPos]

    def hasPrevious(self):
        """如果列表迭代器还有上一个item则返回True,否则返回False."""
        return self._cursor > 0

    def previous(self):
        """前提: hasPrevious()返回True.
        除了迭代器的mutators外,这个列表还没有被修改过.
        返回当前item并移动cursor到上一个item."""
        if not self.hasPrevious():
            raise ValueError("no previous item in list iterator")
        if self._modCount != self._backingStore.getModCount():
            raise AttributeError("illegal modification of backing store")
        self._cursor -= 1
        self._lastItemPos = self._cursor
        return self._backingStore[self._lastItemPos]