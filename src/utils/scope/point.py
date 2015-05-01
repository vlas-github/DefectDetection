#!/usr/bin/env python
# -*- coding: utf-8 -*-


# todo сделать методы from_tuple и from_list


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