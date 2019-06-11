# encoding: utf-8

"""
File: cashfactory.py
Author: Rock Johnson
"""
import re
from .cash import *


class CashFactory:
    def create_cash_accept(self, type):
        cash_return = re.findall('满(\d+)反(\d+)', type)
        cash_rebate = re.findall('打(\d+)折', type)

        if type == '正常收费':
            cs = CashNormal()
        elif cash_return:
            cs = CashReturn(int(cash_return[0][0]), int(cash_return[0][1]))
        elif cash_rebate:
            cs = CashRebate(float(cash_rebate[0]))
        else:
            raise KeyError('类型错误!')
        return cs