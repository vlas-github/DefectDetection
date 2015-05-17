#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: -


class Point():
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def set_x(self, x):
        self._x = x

    def set_y(self, y):
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def to_tuple(self):
        return self._x, self._y

    def to_list(self):
        return [self._x, self._y]

    @staticmethod
    def from_tuple(t):
        return Point(t[0], t[1])

    @staticmethod
    def from_list(t):
        return Point(t[0], t[1])