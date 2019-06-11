# encoding: utf-8

"""
File: operation.py
Author: Rock Johnson
"""
class Operation:
    def __init__(self, number_a, number_b):
        self._number_a = number_a
        self._number_b = number_b
        self._result = 0

    def get_result(self):
        pass


class OperationAdd(Operation):
    def get_result(self):
        self._result = self._number_a + self._number_b
        return self._result


class OperationSub(Operation):
    def get_result(self):
        self._result = self._number_b - self._number_b
        return self._result


class OperationMul(Operation):
    def get_result(self):
        self._result = self._number_a * self._number_b
        return self._result


class OperationDiv(Operation):
    def get_result(self):
        if self._number_b == 0:
            raise ZeroDivisionError('被除数不能为0')
        self._result = self._number_a / self._number_b
        return self._result