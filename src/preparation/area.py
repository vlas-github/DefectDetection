#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Выделение области вокруг точки сканирования
"""

# TODO: Убрать магические числа


import src.utils.other.functions as f


def get_area(scope):
    point = scope.get_point()
    work_image = scope.get_work_image()
    scale = scope.get_scale()
    width = scope.get_allowed_width()

    radius = scale * width * 2.5
    diameter = 2 * radius

    in_circle = lambda p: f.in_circle(radius, p)

    area = [[-1 for _ in range(0, int(diameter))] for _ in range(0, int(diameter))]

    for x in xrange(0, int(diameter)):
        for y in xrange(0, int(diameter)):
            if in_circle((x - radius, y - radius)):
                area[x][y] = work_image[int(y + point.get_y() - radius)][int(x + point.get_x() - radius)]

    return area


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

    start(_scope)
    _area = get_area(_scope)