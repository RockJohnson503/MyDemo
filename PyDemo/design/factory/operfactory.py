# encoding: utf-8

"""
File: factory.py
Author: Rock Johnson
"""
from .operation import *

class OperationFactory:
    def create_operate(self, number_a, number_b, operate):
        args = number_a, number_b
        if operate == '+':
            return OperationAdd(*args)
        elif operate == '-':
            return OperationSub(*args)
        elif operate == '*':
            return OperationMul(*args)
        elif operate == '/':
            return OperationDiv(*args)
        else:
            raise KeyError('请输入正确的操作符!')