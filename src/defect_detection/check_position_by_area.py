#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка координат точки
"""

# TODO: -


from src.utils.other.functions import degrees_to_radians
from src.utils.other.functions import vector_value_and_direction_coordinates


def check(scope, area):
    area_height = len(area)
    area_width = len(area[0])

    height_mid = area_height / 2
    width_mid = area_width / 2

    tl = tr = br = bl = 0

    for x in xrange(0, area_height):
        for y in xrange(0, area_width):
            if area[x][y] != -1 and area[x][y] != 255:
                if x < height_mid and y < width_mid:
                    tl += 0
                elif x > height_mid and y < width_mid:
                    tr += 0
                elif x > height_mid and y > width_mid:
                    br += 0
                else:
                    bl += 0

    v1 = vector_value_and_direction_coordinates(tl, degrees_to_radians(45))
    v2 = vector_value_and_direction_coordinates(tr, degrees_to_radians(135))
    v3 = vector_value_and_direction_coordinates(bl, degrees_to_radians(225))
    v4 = vector_value_and_direction_coordinates(br, degrees_to_radians(315))

    return reduce(lambda (res_x, res_y), (x, y): (res_x + x, res_y + y), [v1, v2, v3, v4], (0, 0))
