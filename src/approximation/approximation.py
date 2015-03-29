#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    По обработанному изображению определяетнаправление линии шва
"""


import cv2
import numpy as np
import math


def get_perpendicular(scope):
    image = scope.work_image
    point = scope.point

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    h, w = closed.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(closed, mask, point.to_tuple(), (255, 0, 255))

    line = get_line_in_circle(closed, point, 20)

    return equation_of_perpendicular(line, point.to_tuple())


def get_line_in_circle(img, point, radius):
    fault = radius / 10
    point1 = (-1, -1)
    point2 = (-1, -1)
    for f in range(0, 360):
        x = int(math.sin(f) * radius + point.get_x())
        y = int(math.cos(f) * radius + point.get_y())
        if img[y][x] == 255:
            if point1[0] == -1 and point1[1] == -1:
                point1 = (x, y)
            elif abs(point1[0] - x) < fault and abs(point1[1] - y) < fault:
                point1 = (point1[0] + x) / 2, (point1[1] + y) / 2
            elif point2[0] == -1 and point2[1] == -1:
                point2 = (x, y)
            else:
                point2 = (point2[0] + x) / 2, (point2[1] + y) / 2
    return point1, point2


def equation_of_perpendicular(line, point):
    ((x1, y1), (x2, y2)) = line
    (x, y) = point
    vector1 = - (y1 - y),  x1 - x
    vector2 = - (y2 - y), x2 - x
    ((x1, y1), (x2, y2)) = (vector1[0] + x, vector1[1] + y), (vector2[0] + x, vector2[1] + y)
    print ((x1, y1), (x2, y2))
    return lambda arg: (y2 - y1) * (arg - x1) / (x2 - x1) + y1


if __name__ == '__main__':
    from src.utils.scope.scope import Scope
    from src.utils.scope.point import Point
    from src.utils.scope.rectangle import Rectangle

    _lt = Point(950, 750)
    _rb = Point(1200, 870)
    _point = Point(1000 - 950, 805 - 750)
    _rect = Rectangle(_lt, _rb)
    _scope = Scope()
    _scope.load_image_by_path('../../image/12мм/fc2_save_2014-11-20-154727-0000.bmp')
    _scope.select_area(_rect)
    _scope.select_point(_point)

    from src.edge_detection.canny import start

    start(_scope)
    foo = get_perpendicular(_scope)
    _image = _scope.work_image

    for i in range(-100, 100):
        _x = _point.get_x() + i / 100.0
        _y = foo(_x)
        cv2.circle(_image, (int(_x), int(_y)), 1, (255, 255, 255), 1, 8)

    cv2.imshow('image', _image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()