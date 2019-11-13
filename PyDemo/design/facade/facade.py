# encoding: utf-8

"""
File: stock.py
Author: Rock Johnson
"""
class Stock1:
    def sell(self):
        print('股票1卖出')

    def buy(self):
        print('股票1买入')


class Stock2:
    def sell(self):
        print('股票2卖出')

    def buy(self):
        print('股票2买入')


class Stock3:
    def sell(self):
        print('股票3卖出')

    def buy(self):
        print('股票3买入')


class NationalDebt1:
    def sell(self):
        print('国债1卖出')

    def buy(self):
        print('国债1买入')


class Realty1:
    def sell(self):
        print('房地产1卖出')

    def buy(self):
        print('房地产1买入')


class Fund:
    def __init__(self):
        self.g1 = Stock1()
        self.g2 = Stock2()
        self.g3 = Stock3()
        self.n1 = NationalDebt1()
        self.r1 = Realty1()

    def buy(self):
        self.g1.buy()
        self.g2.buy()
        self.g3.buy()
        self.n1.buy()
        self.r1.buy()

    def sell(self):
        self.g1.sell()
        self.g2.sell()
        self.g3.sell()
        self.n1.sell()
        self.r1.sell()


if __name__ == '__main__':
    f = Fund()
    f.buy()
    f.sell()