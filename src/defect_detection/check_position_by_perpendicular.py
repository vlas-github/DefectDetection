#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка координат точки
"""

# TODO: Написать тесты


from src.utils.other.functions import length


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

    point_1_to_point = length(point_1, point.to_tuple())
    point_2_to_point = length(point_2, point.to_tuple())

    distance = abs(point_1_to_point - point_2_to_point) / 2
    direction = (point_1[0] + point_2[0], point_1[1] + point_2[1])

    return distance, direction


if __name__ == '__main__':
    pass
