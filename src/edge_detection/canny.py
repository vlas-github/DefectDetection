#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Выделение контура с помощью Цепного кода Фримена
"""


from src.utils.scope.scope import Scope
import cv2
import numpy as np


def start(scope):
    image = scope.work_image
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 1, 1)
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    closed = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
    for i in range(1, 10):
        cv2.imshow("Image", canny)
        cv2.waitKey(0)
        cv2.imshow("Image", closed)
        cv2.waitKey(0)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
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

