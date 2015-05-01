#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    По обработанному изображению определяетнаправление линии шва
"""

# TODO: -


import cv2
import math
import sympy
from src.utils.other.functions import degrees_to_radians


def get_perpendicular(scope):
    """
    Определение перпендикуляра к шву
    :param scope: Рабочее изображение и точка сканирования
    :return: Перпендикуляр к шву в точке сканирования
    """
    work_image = scope.get_work_image()
    point = scope.get_point()

    # Получаем список точек на контуре
    points = get_points_on_circle(work_image, point, 20)
    points += get_points_on_circle(work_image, point, 25)
    points += get_points_on_circle(work_image, point, 30)

    # Проводи процедуру интерполяции
    line = interpolate(points)

    # Возвращаем перпендикуляр к шву
    return equation_of_perpendicular(line, point.to_tuple())


def get_points_on_circle(img, center, radius):
    """
    Определяет точки пересечения шва и окружности
    :param img: Рабочее изображение шва
    :param center: Точка для анализа
    :param radius: Радиус окружности
    :return: Две точки принадлежащие и окружности и шву
    """
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
    """
    Определяет перпендикуляр к линии в точке по формуле (x) -> f(x0) - 1/f'(x0) * (x - x0)
    :param line: Исходное уравнение линии
    :param point: Точка в которой нужно построить перпендикуляр
    :return: Уравнение перпендикуляра
    """
    x = sympy.symbols('x')
    diff = sympy.diff(line, x)
    y_0 = line.evalf(subs={x: point[0]})
    return lambda arg: -1 / diff.evalf(subs={x: point[0]}) * (arg - point[0]) + y_0


def interpolate(points):
    """
    Интерполяция функции с помощью библиотеки sympy
    :param points: Точки на линии
    :return: Уравнение линии проходящей через заданные точки
    """
    x = sympy.symbols('x')
    return sympy.interpolate(points, x)


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
    foo = get_perpendicular(_scope)
    _image = _scope.get_work_image()

    for i in range(-100, 100):
        _x = _point.get_x() + i / 100.0
        _y = foo(_x)
        cv2.circle(_image, (int(_x), int(_y)), 1, (255, 255, 255), 1, 8)

    cv2.imshow('image', _image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()