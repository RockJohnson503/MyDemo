# encoding: utf-8

"""
File: baginterface.py
Author: Rock Johnson
"""
class BagInterface(object):
    """所有包类型的接口."""

    # 构造函数
    def __init__(self, sourceCollection = None):
        """初始状态,其中包括sourceCollection的内容(如果存在)."""
        pass

    # 进行访问的方法
    def isEmpty(self):
        """当len(self) == 0时返回True,否则返回False."""
        return True

    def __len__(self):
        """返回self的长度."""
        return 0

    def __str__(self):
        """将self以字符串的形式表现."""
        return ""

    def __iter__(self):
        """支持将self进行迭代."""
        return None

    def __add__(self, other):
        """返回一个包含self以及other的新bag."""
        return None

    def __eq__(self, other):
        """当self等于other时返回True,否者返回False."""
        return False

    # 赋值的函数
    def clear(self):
        """使self变为空的."""
        pass

    def add(self, item):
        """将item添加进self."""
        pass

    def remove(self, item):
        """前提: item在self里面.
        Raises: KeyError如果item不在self里面.
        后置条件: 将item从self中移除."""
        pass