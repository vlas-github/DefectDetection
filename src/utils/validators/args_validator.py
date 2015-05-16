#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Модуль для валидации исходных данных для запуска приложения
"""

# TODO: -


import os.path
from src.utils.log import log


def args_validator(fn):
    """
    Декоратор для валидации исходных данных для запуска приложения
    :param fn: Функция аргументы которой нужно валидировать
    :return: Функция обернутая в декоратор, который валидирует исходные аргументы
    """
    def wrapped(args):
        if os.path.exists(args.image):
            log.error('image not found')
        elif len(args.area) != 4:
            log.error('area format is incorrect')
        elif len(args.point) != 2:
            log.error('point format is incorrect')
        elif len(args.size) != 2:
            log.error('size format is incorrect')
        elif args.type != 0 and args.type != 1 and args.type != 2:
            log.error('invalid type')
        else:
            fn(args)
    return wrapped