#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Модуль запускающий приложение
"""

# TODO: -


import sys
import argparse
import src.utils.scope.scope as s
import src.approximation.approximation as approximation
import src.edge_detection.canny as canny
import src.defect_detection.check_position as check_position
import src.defect_detection.check_width as check_width
import src.defect_detection.analyze_results as analyze_results
from src.utils.validators.args_validator import args_validator

sys.path.append(u'/home/vlasov-id-131216/Dropbox/Универ/Диплом/project/DefectDetection/')


@args_validator
def main_console(args):
    area = s.Rectangle(s.Point(args.area[0], args.area[1]),
                       s.Point(args.area[2], args.area[3]))
    point = s.Point(args.point[0], args.point[1])
    scope = s.Scope()
    scope.load_image_by_path(args.image)
    scope.select_area(area)
    scope.select_point(point)
    scope.set_area_color(255, 0, 0)
    scope.set_point_color(0, 0, 255)
    scope.set_size(args.size[0], args.size[1])

    canny.start(scope)
    perpendicular = approximation.get_perpendicular(scope)

    check_position_result = check_position.check(scope, perpendicular)
    check_width_result = check_width.check(scope, perpendicular)
    return analyze_results.analyze(check_position_result, check_width_result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode',  help='way to run (gui or console)', default='console')
    parser.add_argument('-i', '--image', help='path to image')
    parser.add_argument('-a', '--area',  help='work area (-a x1 y1 x2 y2)',  nargs='+', type=int)
    parser.add_argument('-p', '--point', help='point (-p x y)',              nargs='+', type=int)
    parser.add_argument('-s', '--size',  help='image size in mm (-i h w)',   nargs='+', type=float)
    _args = parser.parse_args()
    if _args.mode == 'console':
        main_console(_args)