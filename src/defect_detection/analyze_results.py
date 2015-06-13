#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Анализзирует результат и возвращает инструкцию для продолжения работы
"""

# TODO: -


import math
from src.utils.other import result_codes


def analyze_width_by_perpendicular(scope, real_width):
    scale = scope.get_scale()
    width = scope.get_allowed_width()

    if real_width > scale * width:
        return [1]
    else:
        return [0]


def analyze_width_by_area(scope, result):
    if result:
        return [0]
    else:
        return [1]


def analyze_position_by_perpendicular(scope, result):
    distance, direction = result
    results = []
    width = scope.get_allowed_width()
    distance = distance / width

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


def analyze_position_by_area(scope, result):
    results = [get_direction(result)]
    distance = math.sqrt(result[0] ** 2 + result[1] ** 2)
    if distance < 0.2:
        results.append(result_codes.LITTLE)
    elif distance < 0.5:
        results.append(result_codes.MID)
    elif distance < 0.8:
        results.append(result_codes.MANY)
    return results


def get_direction(vector):
    m = [(0.00,   result_codes.R),    (22.50,  result_codes.TRR),  (45.00,  result_codes.TR),
         (67.50,  result_codes.TTR),  (90.00,  result_codes.T),    (112.50, result_codes.TTL),
         (135.00, result_codes.TL),   (157.50, result_codes.TLL),  (180.00, result_codes.L),
         (202.50, result_codes.BLL),  (225.00, result_codes.BL),   (247.50, result_codes.BBL),
         (270.00, result_codes.B),    (292.50, result_codes.BBR),  (315.00, result_codes.BR),
         (337.50, result_codes.BRR)]
    direction = math.atan(vector[0] / vector[1])
    return filter(lambda (d, _): direction - 11.15 <= d <= direction + 11.15, m)[0][1]