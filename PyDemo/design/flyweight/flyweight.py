# encoding: utf-8

"""
File: flyweight.py
Author: Rock Johnson
"""
class Coffee:
    def __init__(self, name):
        self.name = name
        self.price = len(name)

    def show(self):
        print('%s咖啡, 价格:' % self.name, self.price)


class CoffeeFactory:
    coffee_dt = {}

    def get_coffee(self, name):
        if not self.coffee_dt.get(name):
            self.coffee_dt[name] = Coffee(name)
        return self.coffee_dt[name]

    def count_coffee(self):
        return len(self.coffee_dt)


class Customer:
    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print('%s 点了一杯咖啡:' % self.name, coffee_name)
        return self.coffee_factory.get_coffee(coffee_name)


if __name__ == '__main__':
    cf = CoffeeFactory()
    c1 = Customer('顾客A', cf)
    c2 = Customer('顾客B', cf)
    c3 = Customer('顾客C', cf)
    c1_cp = c1.order('卡布奇诺')
    c1_cp.show()
    c2_cp = c2.order('摩卡')
    c2_cp.show()
    c3_cp = c3.order('卡布奇诺')
    c3_cp.show()

    print('实例化了%d种咖啡' % cf.count_coffee())