#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Проверка координат точки
"""

# TODO: - Сделать нормализацию вектора
# TODO: - Проверить координаты х и у


from src.utils.other.functions import vector_value_and_direction_coordinates


white_color = 255


def check(scope, area):
    area_height = len(area)
    area_width = len(area[0])

    height_mid = area_height / 2
    width_mid = area_width / 2

    tl = tr = br = bl = 0

    for x in xrange(0, area_height):
        for y in xrange(0, area_width):
            if area[x][y] != -1 and area[x][y] != white_color:
                if x < height_mid and y < width_mid:
                    tl += 1
                elif x > height_mid and y < width_mid:
                    tr += 1
                elif x > height_mid and y > width_mid:
                    br += 1
                else:
                    bl += 1

    v1 = vector_value_and_direction_coordinates(tl, 45)
    v2 = vector_value_and_direction_coordinates(tr, 135)
    v3 = vector_value_and_direction_coordinates(bl, -135)
    v4 = vector_value_and_direction_coordinates(br, -45)

    max_width = max(tl, tr, bl, br)
    result = reduce(lambda (res_x, res_y), (_x, _y): (res_x + _x, res_y + _y), [v1, v2, v3, v4], (0, 0))

    return result[0] / max_width, result[1] / max_width


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