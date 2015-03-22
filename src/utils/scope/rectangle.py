#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Представление рабочей области в виде прямоугольника
    Прямоугольник задается двумя точками (лево-верх, право-низ)
"""


# todo сделать валидацию входных данных
# todo сделать методы from_tuple и from_list


class Rectangle():
    def __init__(self, left_top_point, right_bot_point):
        self.lt = left_top_point
        self.rb = right_bot_point

    def set_left_top(self, point):
        self.lt = point

    def set_right_bot(self, point):
        self.rb = point

    def get_left_top(self):
        return self.lt

    def get_right_bot(self):
        return self.rb

    def to_tuple(self):
        return self.lt.to_tuple(), self.rb.to_tuple()

    def to_list(self):
        return [self.lt.to_list(), self.rb.to_list()]