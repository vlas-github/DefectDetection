#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: add exceptions


import cv2
from rectangle import Rectangle
from point import Point
from src.utils.config.config import full_path


class Scope():
    def __init__(self):
        self._base_image = ()
        self._work_image = ()
        self._area = ()
        self._point = ()
        self._area_color = (255, 0, 0)
        self._point_color = (0, 255, 0)
        self._size = ()
        self._allowed_width = 2
        self._scale = 2

    def load_image_by_path(self, path):
        self._base_image = cv2.imread(full_path(path))

    def select_area(self, rectangle):
        self._area = rectangle
        (x1, y1), (x2, y2) = self._area.to_tuple()
        self._work_image = self._base_image[y1:y2, x1:x2]

    def set_work_image(self, work_image):
        self._work_image = work_image

    def select_point(self, point):
        self._point = point

    def set_area_color(self, r, g, b):
        self._area_color = (r, g, b)

    def set_point_color(self, r, g, b):
        self._point_color = (r, g, b)

    def set_size(self, x, y):
        self._size = (x, y)

    def set_scale(self, scale):
        self._scale = scale

    def set_allowed_width(self, allowed_width):
        self._allowed_width = allowed_width

    def get_area_color(self):
        return self._area_color

    def get_point_color(self):
        return self._point_color

    def get_image(self):
        return self._base_image

    def get_work_image(self):
        return self._work_image

    def get_area(self):
        return self._area

    def get_point(self):
        return self._point

    def get_size(self):
        return self._size

    def get_scale(self):
        return self._scale

    def get_allowed_width(self):
        return self._allowed_width


if __name__ == '__main__':
    """
        Тесты и пример работы модуля
    """
    _lt = Point(950, 600)
    _rb = Point(1200, 900)
    _point = Point(1000, 800)
    _rect = Rectangle(_lt, _rb)
    _scope = Scope()
    _scope.load_image_by_path('image/Defective/12257157-2015-02-10-105717.png')
    _scope.select_area(_rect)
    _scope.select_point(_point)
    _image = _scope.get_work_image()
    cv2.imshow('image', _image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()