# encoding: utf-8

"""
File: builder.py
Author: Rock Johnson
"""
class PersonBuilder:
    def __init__(self, g, p):
        self.g = g
        self.p = p

    def build_head(self): pass

    def build_body(self): pass

    def build_arm_left(self): pass

    def build_arm_right(self): pass

    def build_leg_left(self): pass

    def build_leg_right(self): pass


class PersonDirector:
    def __init__(self, pb: PersonBuilder):
        self.pb = pb

    def create_person(self):
        self.pb.build_head()
        self.pb.build_body()
        self.pb.build_arm_left()
        self.pb.build_arm_right()
        self.pb.build_leg_left()
        self.pb.build_leg_right()

class PersonThinBuilder(PersonBuilder):
    def __init__(self, g, p):
        super().__init__(g, p)

    def build_head(self):
        print('创建头: 50, 20, 30, 30; 使用背景: %s, 使用的笔: %s' % (self.g, self.p))

    def build_body(self):
        print('创建身体: 60, 50, 10, 50; 使用背景: %s, 使用的笔: %s' % (self.g, self.p))

    def build_arm_left(self):
        print('创建左手: 60, 50, 40, 100; 使用背景: %s, 使用的笔: %s' % (self.g, self.p))

    def build_arm_right(self):
        print('创建右手: 70, 50, 90, 100; 使用背景: %s, 使用的笔: %s' % (self.g, self.p))

    def build_leg_left(self):
        print('创建左腿: 60, 100, 45, 150; 使用背景: %s, 使用的笔: %s' % (self.g, self.p))

    def build_leg_right(self):
        print('创建右腿: 70, 100, 85, 150; 使用背景: %s, 使用的笔: %s' % (self.g, self.p))


if __name__ == '__main__':
    pd = PersonDirector(PersonThinBuilder('白色背景', '黑色钢笔'))
    pd.create_person()
