# encoding: utf-8

"""
File: work.py
Author: Rock Johnson
"""
import copy


class WorkExperience:
    def __init__(self):
        self.time_area = None
        self.company = None

    def clone(self):
        return copy.copy(self)