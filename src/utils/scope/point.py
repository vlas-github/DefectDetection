#!/usr/bin/env python
# -*- coding: utf-8 -*-


# todo сделать методы from_tuple и from_list


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def to_tuple(self):
        return self.x, self.y

    def to_list(self):
        return [self.x, self.y]