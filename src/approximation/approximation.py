#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    По обработанному изображению определяетнаправление линии шва
"""

# TODO: -


import cv2
import numpy as np
import math
import sympy


def get_perpendicular(scope):
    image = scope.work_image
    point = scope.point

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    h, w = closed.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(closed, mask, point.to_tuple(), (255, 0, 255))

    for x in xrange(0, w):
        for y in xrange(0, h):
            if closed[y][x] != 255:
                closed[y][x] = 0

    points = get_points_on_circle(closed, point, 20)
    points += get_points_on_circle(closed, point, 25)
    points += get_points_on_circle(closed, point, 30)
    line = interpolate(points)
    return equation_of_perpendicular(line, point.to_tuple())


def get_points_on_circle(img, center, radius):
    points = []
    old_point_color = 0

    for degrees in range(0, 360):
        radians = degrees_to_radians(degrees)
        x = int(math.sin(radians) * radius + center.get_x())
        y = int(math.cos(radians) * radius + center.get_y())
        if old_point_color != img[y][x]:
            if old_point_color == 255:
                points.append(((old_point[0] + x) / 2, (old_point[1] + y) / 2))
            old_point_color = img[y][x]
            old_point = (x, y)

    return points


def equation_of_perpendicular(line, point):
    x = sympy.symbols('x')
    diff = sympy.diff(line, x)
    y_0 = line.evalf(subs={x: point[0]})
    return lambda arg: -1 / diff.evalf(subs={x: point[0]}) * (arg - point[0]) + y_0


def degrees_to_radians(degrees):
    return degrees * math.pi / 180.0


def interpolate(points):
    x = sympy.symbols('x')
    return sympy.interpolate(points, x)


if __name__ == '__main__':
    from src.utils.scope.scope import Scope
    from src.utils.scope.point import Point
    from src.utils.scope.rectangle import Rectangle

    _lt = Point(950, 750)
    _rb = Point(1200, 870)
    _point = Point(1000 - 950, 805 - 750)
    _rect = Rectangle(_lt, _rb)
    _scope = Scope()
    _scope.load_image_by_path('image/12мм/fc2_save_2014-11-20-154727-0000.bmp')
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