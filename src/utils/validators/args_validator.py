#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Модуль для валидации исходных данных для запуска приложения
"""


# todo Пролумать нормальную валидацию


import os.path
from src.utils.log.log import error


def args_validator(fn):
    """
    Декоратор для валидации исходных данных для запуска приложения
    :param fn: Функция аргументы которой нужно валидировать
    :return: Функция обернутая в декоратор, который валидирует исходные аргументы
    """
    def wrapped(args):
        if args.mode != 'console' or args.mode != 'gui':
            error('unidentified mode')
        elif os.path.exists(args.image):
            error('image not found')
        elif len(args.area) != 4:
            error('area format is incorrect')
        elif len(args.pint) != 2:
            error('point format is incorrect')
        elif len(args.size) != 2:
            error('size format is incorrect')
        else:
            fn(args)
    return wrapped