#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка ширины шва
"""

# TODO: -


import math


def check(scope, perpendicular):
    work_image = scope.get_work_image()
    point = scope.get_point()
    scale = scope.get_scale()
    width = scope.get_allowed_width()

    old_color = 0
    for i in xrange(-100, 100):
        x = point.get_x() + width * i / 200.0
        y = perpendicular(x)
        color = work_image[int(y)][int(x)]
        if color == 255 and old_color != 255:
            point_1 = (x, y)
        if color != 255 and old_color == 255:
            point_2 = (x, y)
        old_color = color

    real_width = math.sqrt(math.pow(point_1[0] - point_2[0], 2) + math.pow(point_1[1] - point_2[1], 2))

    if real_width > scale * width:
        return False
    else:
        return True