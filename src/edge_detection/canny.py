#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Выделение контура
"""

# todo доработать алгоритм


import cv2
import numpy as np


def start(scope):
    image = scope.work_image
    noise = cv2.fastNlMeansDenoising(image, None, 9, 3, 9)
    blurred = cv2.GaussianBlur(noise, (3, 3), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 1, 1)
    kernel = np.ones((2, 2), np.float32) / 5
    dst = cv2.filter2D(canny, -1, kernel)
    scope.work_image = dst


if __name__ == '__main__':
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
        cv2.imshow("Image", _scope.work_image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()


