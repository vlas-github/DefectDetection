#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Выделение области вокруг точки сканирования
"""

# TODO: -


import math as m


def length((x1, y1), (x2, y2)):
    return m.sqrt(m.pow(x2 - x1, 2) + m.pow(y2 - y1, 2))


def in_circle(radius, point):
    x, y = point
    return m.sqrt(x * x + y * y) <= radius