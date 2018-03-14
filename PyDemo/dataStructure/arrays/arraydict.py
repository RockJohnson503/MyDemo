# encoding: utf-8

"""
File: arraydict.py
Author: Rock Johnson
"""
from dataStructure.abstracts.abstractdict import AbstractDict, Item

class ArrayDict(AbstractDict):
    """基于array的dict实现."""

    def __init__(self, sourceCollection=None):
        """如果存在,则将item从sourceCollection复制到集合中."""
        AbstractDict.__init__(self, sourceCollection)

    # 访问方法
    def __iter__(self):
        """提供字典中的keys."""
        cursor = 0
        while cursor < len(self):
            yield self._items[cursor].key
            cursor += 1

    def __getitem__(self, key):
        """前提: key在字典里面.
        Raises: 如果key不在字典里则抛出KeyError.
        返回与该key关联的value."""
        index = self._index(key)
        if index == -1:
            raise KeyError("missing: " + str(key))
        return self._items[index].value

    # 赋值方法
    def __setitem__(self, key, value):
        """如果key不在字典里,则将key和value添加进去.
        否则将久的值与新的值替换掉."""
        index = self._index(key)
        if index == -1:
            self._items.append(Item(key, value))
            self._size += 1
        else:
            self._items[index].value = value

    def pop(self, key):
        """前提: key在字典里.
        Raises: 如果key不在字典里则抛出KeyError.
        如果key在字典里则移除key并返回可以这个key关联的value,
        否则返回默认的value."""
        index = self._index(key)
        if index == -1:
            raise KeyError("missing: " + str(key))
        self._size -= 1
        return self._items.pop(index).value

    def _index(self, key):
        """搜索key的一个辅助方法."""
        index = 0
        for entry in self._items:
            if entry.key == key:
                return index
            index += 1
        return -1