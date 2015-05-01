#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка ширины шва
"""

# TODO: -


import cv2
import numpy as np
import math


def check(scope, perpendicular):
    work_image = scope.get_work_image()
    point = scope.get_point()
    scale = scope.get_scale()
    width = scope.get_allowed_width()

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(work_image, cv2.MORPH_CLOSE, kernel)

    h, w = closed.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(closed, mask, point.to_tuple(), (255, 0, 255))

    for x in xrange(0, w):
        for y in xrange(0, h):
            if closed[y][x] != 255:
                closed[y][x] = 0

    old_color = 0
    for i in xrange(-100, 100):
        x = point.get_x() + width * i / 200.0
        y = perpendicular(x)
        color = closed[int(y)][int(x)]
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