# encoding: utf-8

"""
File: bridge.py
Author: Rock Johnson
"""
# 手机软件
class HandsetSoft:
    def run(self): pass


class HandsetGame(HandsetSoft):
    def run(self):
        print('运行游戏')


class HandsetAddressList(HandsetSoft):
    def run(self):
        print('运行通讯录')


class HandsetMP3(HandsetSoft):
    def run(self):
        print('运行MP3')


# 手机品牌
class HandsetBrand:
    def set_handset_soft(self, soft):
        self.soft = soft

    def run(self): pass


class HandsetBrandN(HandsetBrand):
    def run(self):
        self.soft.run()


class HandsetBrandM(HandsetBrand):
    def run(self):
        self.soft.run()


if __name__ == '__main__':
    hn = HandsetBrandN()
    hn.set_handset_soft(HandsetGame())
    hn.run()