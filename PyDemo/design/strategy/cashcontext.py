# encoding: utf-8

"""
File: cashcontent.py
Author: Rock Johnson
"""
import re
from .cash import *


class CashContext:
    def __init__(self, type):
        cash_return = re.findall('满(\d+)反(\d+)', type)
        cash_rebate = re.findall('打(\d+)折', type)

        if type == '正常收费':
            cash = CashNormal()
        elif cash_return:
            cash = CashReturn(cash_return[0][0], cash_return[0][1])
        elif cash_rebate:
            cash = CashRebate(cash_rebate[0])
        else:
            raise KeyError('类型错误!')
        self._cs = cash

    def get_result(self, money):
        if isinstance(money, int) and money >= 0:
            return self._cs.accept_cash(money)
        else:
            raise KeyError('请输入有效的付款金额!')