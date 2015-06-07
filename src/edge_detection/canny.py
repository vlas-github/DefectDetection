#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Выделение контура
"""

# TODO: Доработать алгоритм


import cv2
import numpy as np
from src.utils.log import log


def start(scope):
    image = scope.get_work_image()
    point = scope.get_point()
    noise = cv2.fastNlMeansDenoising(image, None, 9, 3, 9)
    blurred = cv2.GaussianBlur(noise, (3, 3), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)

    canny = cv2.Canny(gray, 1, 1)
    kernel = np.ones((2, 2), np.float32) / 5
    dst = cv2.filter2D(canny, -1, kernel)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(dst, cv2.MORPH_CLOSE, kernel)

    h, w = closed.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    cv2.floodFill(closed, mask, point.to_tuple(), (255, 0, 255))

    count_white_pixels = 0

    for x in xrange(0, w):
        for y in xrange(0, h):
            if closed[y][x] != 255:
                closed[y][x] = 0
            else:
                count_white_pixels += 1

    if count_white_pixels < len(closed[0]) * scope.get_scale() * scope.get_allowed_width():
        log.error('invalid weld point')
        raise ValueError('invalid weld point')

    scope.set_work_image(closed)


if __name__ == '__main__':
    """
        Тесты и пример работы модуля
    """
    from src.utils.scope.scope import Scope
    from src.utils.scope.point import Point
    from src.utils.scope.rectangle import Rectangle
    _lt = Point(950, 750)
    _rb = Point(1200, 870)
    _point = Point(1000, 800)
    _rect = Rectangle(_lt, _rb)
    _scope = Scope()
    _scope.load_image_by_path('../../image/12мм/fc2_save_2014-11-20-154727-0000.bmp')
    _scope.select_area(_rect)
    _scope.select_point(_point)
    start(_scope)
    for i in range(1, 4):
        cv2.imshow("Image", _scope.get_work_image())
        cv2.waitKey(0)
    cv2.destroyAllWindows()


