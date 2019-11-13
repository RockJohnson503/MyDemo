# encoding: utf-8

"""
File: adapter.py
Author: Rock Johnson
"""
class Adapter:
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()


class Adaptee:
    def specific_request(self):
        print('调用了适配者的specific请求')


if __name__ == '__main__':
    ae = Adaptee()
    ar = Adapter(ae)
    ar.request()