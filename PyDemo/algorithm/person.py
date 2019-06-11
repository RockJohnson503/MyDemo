# encoding: utf-8

"""
File: person.py
Author: Rock Johnson
"""
from collections import deque


class Person:
    def __init__(self, name, job):
        self.__name = name
        self.__job = job
        self.__friends = []

    def __str__(self):
        return self.__name

    @property
    def job(self):
        return self.__job

    @property
    def friends(self):
        return self.__friends

    def remove_friend(self, friend):
        if not isinstance(friend, Person):
            raise TypeError('的朋友不是人类!')

    def add_friend(self, friend):
        if not isinstance(friend, Person):
            raise TypeError('添加的朋友不是人类!')
        self.__friends.insert(0, friend)

    def add_friends(self, friends):
        if not isinstance(friends, (tuple, list, set)):
            raise TypeError('不是可迭代对象')
        if len(friends) == 0:
            raise KeyError('添加的朋友列表不可为空')

        for friend in friends:
            self.add_friend(friend)

    def relation_ship(self, job, all=False):
        relations = deque(self.__friends)
        cache = []
        res = []
        while relations:
            friend = relations.popleft()
            cache.append(friend)
            if friend.job == job:
                if all:
                    res.append(friend)
                else:
                    return friend
            if friend.friends:
                for rel_friend in friend.friends:
                    if rel_friend not in cache and rel_friend not in relations and rel_friend != self:
                        relations.append(rel_friend)
        return res if res else None

if __name__ == '__main__':
    me = Person('Rock', '程序员')
    bob = Person('Bob', '服务生')
    alice = Person('Alice', '芒果供应商')
    peggy = Person('Peggy', '学生')
    anuj = Person('Anuj', '老师')
    claire = Person('Claire', '学生')
    jonny = Person('Jonny', '牛奶供应商')
    thom = Person('Thom', '律师')
    tom = Person('Tom', '厨师')
    july = Person('July', '程序员')

    me.add_friends([bob, alice, claire, tom])
    bob.add_friends([anuj, peggy, me])
    peggy.add_friends([bob, alice])
    alice.add_friends([peggy, me])
    claire.add_friends([thom, jonny, me])
    jonny.add_friend(july)

    for friend in me.relation_ship('学生', True):
        print(friend)
    # print(me.relation_ship('学生'))