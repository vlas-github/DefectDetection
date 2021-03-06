#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка ширины шва
"""

# TODO: -


import math


white_color = 255


def check(scope, perpendicular):
    work_image = scope.get_work_image()
    point = scope.get_point()
    width = scope.get_allowed_width()

    old_color = 0
    for i in xrange(-100, 100):
        x = point.get_x() + width * i / 200.0
        y = perpendicular(x)
        color = work_image[int(y)][int(x)]
        if color == white_color and old_color != white_color:
            point_1 = (x, y)
        if color != white_color and old_color == white_color:
            point_2 = (x, y)
        old_color = color

    return math.sqrt(math.pow(point_1[0] - point_2[0], 2) + math.pow(point_1[1] - point_2[1], 2))