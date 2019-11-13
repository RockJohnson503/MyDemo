# encoding: utf-8

"""
File: abstract.py
Author: Rock Johnson
"""
# 电视类
class TV:
    def watch(self): pass


class HaireTV(TV):
    def watch(self):
        print('正在观看海尔电视')


class HisenseTV(TV):
    def watch(self):
        print('正在观看海信电视')


# 冰箱类
class Freezer:
    def open(self): pass


class HaireFreezer(Freezer):
    def open(self):
        print('正在打开海尔冰箱')


class HisenseFreezer(Freezer):
    def open(self):
        print('正在打开海信冰箱')


# 工厂
class Factory:
    def tv(self): pass

    def freezer(self): pass


class Haire(Factory):
    def freezer(self):
        return HaireFreezer()

    def tv(self):
        return HaireTV()


class Hisense(Factory):
    def freezer(self):
        return HisenseFreezer()

    def tv(self):
        return HisenseTV()


if __name__ == '__main__':
    hs = Hisense()
    hsf = hs.freezer()
    hsf.open()

    hr = Haire()
    hrt = hr.tv()
    hrt.watch()