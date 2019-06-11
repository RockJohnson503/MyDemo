# encoding: utf-8

"""
File: cashstrategy.py
Author: Rock Johnson
"""
class Cash:
    def accept_cash(self, money):
        pass


class CashNormal(Cash):
    def accept_cash(self, money):
        return money


class CashRebate(Cash):
    def __init__(self, money_rebate):
        self._money_rebate = float(money_rebate) / 10

    def accept_cash(self, money):
        return money * self._money_rebate


class CashReturn(Cash):
    def __init__(self, money_condition, money_return):
        self._money_condition = int(money_condition)
        self._money_return = int(money_return)

    def accept_cash(self, money):
        pay = money
        if money >= pay:
            pay = money - money // self._money_condition * self._money_return
        return pay