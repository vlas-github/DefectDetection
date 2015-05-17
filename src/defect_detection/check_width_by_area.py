#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка ширины шва
"""

# TODO: -


white_color = 255


def check(scope, area):

    area_height = len(area)
    area_width = len(area[0])

    white_pixel = 0
    other_pixel = 0

    for x in xrange(0, area_height):
        for y in xrange(0, area_width):
            if area[x][y] != -1:
                if area[x][y] == white_color:
                    white_pixel += 1
                else:
                    other_pixel += 1

    if other_pixel >= (white_pixel + other_pixel) / 1.5:
        return False

    white_top = white_bottom = white_left = white_right = False
    for y in xrange(0, area_width):
        if area[area_height - 1][y] == white_color:
            white_bottom = True
        if area[0][y] == white_color:
            white_top = True

    for x in xrange(0, area_height):
        if area[x][area_width - 1] == white_color:
            white_right = True
        if area[x][0] == white_color:
            white_left = True

    result = (not white_bottom and not white_top) or (not white_left and not white_right)
    return result


if __name__ == '__main__':
    """
        Тесты и пример работы модуля
    """
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
    from src.preparation.area import get_area
    start(_scope)
    _area = get_area(_scope)
    _result = check(_scope, _area)
    print _result