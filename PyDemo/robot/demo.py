# encoding: utf-8

"""
File: demo.py
Author: Rock Johnson
"""
from wxpy import *

class Robot:

    def __init__(self):
        self.bot = Bot(cache_path=True)

    def logout(self):
        self.bot.logout()

    def start(self):
        myfriend = self.bot.friends().search("Yuanhua.Jiao")[0]
        print(myfriend)
        details = self.bot.user_details("users")
        print(details.sex())

        # 退出登录
        # self.logout()

    def auto_accept_friends(self):
        @self.bot.register
        def accept(msg):
            if 'wxpy' in msg.text.lower():
                new_friend = msg.card.accept()
                new_friend.send('test')
        return accept

robot = Robot()
robot.start()
# robot.auto_accept_friends()