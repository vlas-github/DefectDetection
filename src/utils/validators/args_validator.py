#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    Модуль для валидации исходных данных для запуска приложения
"""


# todo Пролумать нормальную валидацию


import os.path
from src.utils.log.log import err_log
from src.utils.log.log import info_log
from src.utils.log.log import warn_log


def args_validator(fn):
    """
    Декоратор для валидации исходных данных для запуска приложения
    :param fn: Функция аргументы которой нужно валидировать
    :return: Функция обернутая в декоратор, который валидирует исходные аргументы
    """
    def wrapped(args):
        if args.mode != 'console' or args.mode != 'gui':
            err_log('unidentified mode')
        elif os.path.exists(args.image):
            err_log('image not found')
        elif len(args.area) != 4:
            err_log('area format is incorrect')
        elif len(args.pint) != 2:
            err_log('point format is incorrect')
        elif len(args.size) != 2:
            err_log('size format is incorrect')
        else:
            fn(args)
    return wrapped