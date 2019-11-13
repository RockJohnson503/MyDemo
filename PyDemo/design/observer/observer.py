# encoding: utf-8

"""
File: observer.py
Author: Rock Johnson
"""

# 通知者
class Subject:
    def __init__(self):
        self.subject_state = None
        self.observers = []

    def attach(self, o): pass

    def detach(self, o): pass

    def notify(self): pass


class Boss(Subject):
    def __init__(self):
        super().__init__()

    def attach(self, o):
        self.observers.append(o)

    def detach(self, o):
        self.observers.remove(o)

    def notify(self):
        for o in self.observers:
            o.update()


class Secretary(Subject):
    def __init__(self):
        super().__init__()

    def attach(self, o):
        self.observers.append(o)

    def detach(self, o):
        self.observers.remove(o)

    def notify(self):
        for o in self.observers:
            o.update()


# 观察者
class Observer:
    def __init__(self, name, sub):
        self.name = name
        self.sub = sub

    def update(self): pass


class StockObserver(Observer):
    def __init__(self, name, sub):
        super().__init__(name, sub)

    def update(self):
        print(self.sub.subject_state, self.name, '关闭股票, 继续工作!')


class NBAObserver(Observer):
    def __init__(self, name, sub):
        super().__init__(name, sub)

    def update(self):
        print(self.sub.subject_state, self.name, '关闭NBA直播, 继续工作!')


if __name__ == '__main__':
    huhansan = Boss()

    wgc = StockObserver('魏冠茶', huhansan)
    ygc = NBAObserver('易管差', huhansan)

    huhansan.attach(wgc)
    huhansan.attach(ygc)

    huhansan.detach(wgc)

    huhansan.subject_state = '我胡汉三回来了!'
    huhansan.notify()
