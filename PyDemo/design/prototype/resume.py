# encoding: utf-8

"""
File: resume.py
Author: Rock Johnson
"""
import copy
try:
    from work import WorkExperience
except:
    from .work import WorkExperience


class Resume:
    def __init__(self, name):
        self.name = name
        self.work = WorkExperience()

    # 设置个人信息
    def set_personal_info(self, sex, age):
        self.sex = sex
        self.age = age

    # 设置工作经验
    def set_work_experience(self, time_area, company):
        self.work.time_area = time_area
        self.work.company = company

    # 显示
    def display(self):
        print(self.name, self.sex, self.age)
        print('工作经验: ', self.work.time_area, self.work.company)

    def clone(self):
        obj = copy.copy(self)
        obj.work = self.work.clone()
        return obj


if __name__ == '__main__':
    a = Resume('Rock')
    a.set_personal_info('男', 18)
    a.set_work_experience('2000-2020', 'NASA')

    b = a.clone()
    b.set_work_experience('2001-2015', 'SpaceX')

    c = a.clone()
    c.set_personal_info('女', 20)

    a.display()
    b.display()
    c.display()