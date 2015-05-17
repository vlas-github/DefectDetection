#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Представление рабочей области в виде прямоугольника
    Прямоугольник задается двумя точками (лево-верх, право-низ)
"""


# TODO: -


from src.utils.scope.point import Point


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

    @staticmethod
    def from_tuple(t):
        return Rectangle(Point.from_tuple(t[0]), Point.from_tuple(t[1]))

    @staticmethod
    def from_list(l):
        if len(l) == 2:
            return Rectangle(Point.from_tuple(l[0]), Point.from_tuple(l[1]))
        elif len(l) == 4:
            return Rectangle(Point.from_tuple(l[0:2]), Point.from_tuple(l[3, 4]))