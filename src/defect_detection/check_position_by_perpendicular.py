#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка координат точки
"""

# TODO: Написать тесты


import math
from src.utils.other.functions import length
from src.utils.other import result_codes


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

    return generate_response_code(distance / width, direction)


def generate_response_code(distance, direction):
    results = []
    if distance > 0.1:
        results.append(result_codes.MOVE_POINT)
        if distance < 0.2:
            results.append(result_codes.LITTLE)
        elif distance < 0.3:
            results.append(result_codes.MID)
        elif distance < 0.5:
            results.append(result_codes.MANY)

        results.append(get_direction(direction))

    return results


def get_direction(vector):
    m = [{0.000000,   result_codes.R},    {22.500000,  result_codes.TRR},  {45.000000,  result_codes.TR},
         {67.500000,  result_codes.TTR},  {90.000000,  result_codes.T},    {112.500000, result_codes.TTL},
         {135.000000, result_codes.TL},   {157.500000, result_codes.TLL},  {180.000000, result_codes.L},
         {202.500000, result_codes.BLL},  {225.000000, result_codes.BL},   {247.500000, result_codes.BBL},
         {270.000000, result_codes.B},    {292.500000, result_codes.BBR},  {315.000000, result_codes.BR},
         {337.500000, result_codes.BRR}]
    direction = math.arctan(vector[1] / vector[2])
    return filter(lambda d: direction - 11.15 <= d <= direction + 11.15, m)


if __name__ == '__main__':
    pass
