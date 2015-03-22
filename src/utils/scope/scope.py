#!/usr/bin/env python
# -*- coding: utf-8 -*-


# todo add exceptions


import cv2
from rectangle import Rectangle
from point import Point


class Scope():
    def __init__(self):
        self.base_image = ()
        self.work_image = ()
        self.area = ()
        self.point = ()
        self.area_color = (255, 0, 0)
        self.point_color = (0, 255, 0)
        self.size = ()

    def load_image_by_path(self, path):
        self.base_image = cv2.imread(path)

    def select_area(self, rectangle):
        self.area = rectangle
        (x1, y1), (x2, y2) = self.area.to_tuple()
        self.work_image = self.base_image[y1:y2, x1:x2]

    def select_point(self, point):
        self.point = point

    def set_area_color(self, r, g, b):
        self.area_color = (r, g, b)

    def set_point_color(self, r, g, b):
        self.point_color = (r, g, b)

    def set_size(self, x, y):
        self.size = (x, y)

    def get_area_color(self):
        return self.area_color

    def get_point_color(self):
        return self.point_color

    def get_image(self):
        return self.base_image

    def get_work_image(self):
        return self.work_image

    def get_area(self):
        return self.area

    def get_point(self):
        return self.point

    def get_size(self):
        return self.size

    def get_scale(self):
        pass  # todo


if __name__ == '__main__':
    _lt = Point(950, 600)
    _rb = Point(1200, 900)
    _point = Point(1000, 800)
    _rect = Rectangle(_lt, _rb)
    _scope = Scope()
    _scope.load_image_by_path('../../image/Defective/12257157-2015-02-10-105717.png')
    _scope.select_area(_rect)
    _scope.select_point(_point)
    _image = _scope.get_work_image()
    cv2.imshow('image', _image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()