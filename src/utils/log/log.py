#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Модуль для логирования работы программы
"""

# TODO: -


import logging
from src.utils.config.config import full_path
from src.utils.config.config import get_property


info_log_file = full_path(get_property('log', 'info_log_file', 'logs/info.log'))
error_log_file = full_path(get_property('log', 'error_log_file', 'logs/error.log'))
log = bool(get_property('log', 'log', 'true'))

if log:
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    formatter.datefmt = '%m/%d/%Y %I:%M:%S'

    info_log = logging.getLogger('info_log')
    handler_info_log = logging.FileHandler(info_log_file)
    handler_info_log.setFormatter(formatter)
    info_log.addHandler(handler_info_log)
    info_log.setLevel(logging.INFO)

    error_log = logging.getLogger('error_log')
    handler_error_log = logging.FileHandler(error_log_file)
    handler_error_log.setFormatter(formatter)
    error_log.addHandler(handler_error_log)
    error_log.setLevel(logging.ERROR)


def info(message):
    if log:
        info_log.info(message)
    else:
        print message


def debug(message):
    if log:
        info_log.debug(message)
    else:
        print message


def warning(message):
    if log:
        info_log.warning(message)
    else:
        print message


def error(message):
    if log:
        error_log.error(message)
    else:
        print message


if __name__ == '__main__':
    """
        Тесты и пример работы модуля
    """
    info('info test')
    debug('debug test')
    warning('warning test')
    error('error test')