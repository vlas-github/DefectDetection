#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Модуль запускающий приложение
"""

# TODO: Сделать выбор способа анализа шва (оба)


import sys
import argparse
import src.utils.scope.scope as s
import src.edge_detection.canny as canny
import src.defect_detection.check_position_by_perpendicular as check_position_by_perpendicular
import src.defect_detection.check_width_by_perpendicular as check_width_by_perpendicular
import src.defect_detection.check_position_by_perpendicular as check_position_by_area
import src.defect_detection.check_width_by_perpendicular as check_width_by_area
import src.defect_detection.analyze_results as analyze_results
from src.utils.validators.args_validator import args_validator
from src.utils.config.config import load_config
from src.utils.config.config import full_path
from src.preparation import interpolate
from src.preparation import area

# Добавление модулей приложения в sys.path
sys.path.append(full_path(''))


@load_config
@args_validator
def main_console(args):
    """
    Анализ качества шва в консольном режиме
    :param args: Параметры для работы приложения (фотография детали, область для сканирования и т.д.
    :return: Инструкция к дальнейшим действиям
    """

    # Подготовка исходных данных
    rectangle = s.Rectangle(s.Point(args.area[0], args.area[1]),
                            s.Point(args.area[2], args.area[3]))
    point = s.Point(args.point[0], args.point[1])
    scope = s.Scope()
    scope.load_image_by_path(args.image)
    scope.select_area(rectangle)
    scope.select_point(point)
    scope.set_area_color(255, 0, 0)
    scope.set_point_color(0, 0, 255)
    scope.set_size(args.size[0], args.size[1])

    # Выделение краев и подготовка изображения для анализа
    canny.start(scope)

    # Определение области для сканирования (линия или круг)
    if args.type == 1:
        perpendicular = interpolate.get_perpendicular(scope)

        check_position_result = check_position_by_perpendicular.check(scope, perpendicular)
        check_width_result = check_width_by_perpendicular.check(scope, perpendicular)
    elif args.type == 2:
        a = area.get_area(scope)
        check_position_result = check_position_by_area.check(scope, a)
        check_width_result = check_width_by_area.check(scope, a)
    elif args.type == 0:
        pass

    # Анализ полученных результатов
    return analyze_results.analyze(check_position_result, check_width_result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', help='path to image')
    parser.add_argument('-a', '--area',  help='work area (-a x1 y1 x2 y2)',  nargs='+', type=int)
    parser.add_argument('-p', '--point', help='point (-p x y)',              nargs='+', type=int)
    parser.add_argument('-s', '--size',  help='image size in mm (-i h w)',   nargs='+', type=float)
    parser.add_argument('-t', '--type',  help='1 - perpendicular; 2 - area; 0 - both',  type=int)
    _args = parser.parse_args()
    main_console(_args)