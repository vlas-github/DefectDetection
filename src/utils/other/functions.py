#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Разные математические функции
"""

# TODO: -


import math as m


def length((x1, y1), (x2, y2)):
    return m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2))


def in_circle(radius, point):
    x, y = point
    return m.sqrt(x * x + y * y) <= radius


def degrees_to_radians(degrees):
    return degrees * m.pi / 180.0


def vector_value_and_direction_coordinates(value, direction):
    radians = degrees_to_radians(direction)
    a = m.sqrt(value ** 2 / (1 + m.tan(radians) ** 2))
    b = m.sqrt(value ** 2 - a ** 2)
    if 0 <= direction < 90:
        return a, b
    elif 90 <= direction < 180:
        return -a, b
    elif 180 <= direction < 270:
        return -a, -b
    else:
        return a, -b