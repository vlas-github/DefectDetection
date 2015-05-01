#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Представление рабочей области в виде прямоугольника
    Прямоугольник задается двумя точками (лево-верх, право-низ)
"""


# TODO: сделать валидацию входных данных
# TODO: сделать методы from_tuple и from_list


class Rectangle():
    def __init__(self, left_top_point, right_bot_point):
        self._lt = left_top_point
        self._rb = right_bot_point

    def set_left_top(self, point):
        self._lt = point

    def set_right_bot(self, point):
        self._rb = point

    def get_left_top(self):
        return self._lt

    def get_right_bot(self):
        return self._rb

    def to_tuple(self):
        return self._lt.to_tuple(), self._rb.to_tuple()

    def to_list(self):
        return [self._lt.to_list(), self._rb.to_list()]