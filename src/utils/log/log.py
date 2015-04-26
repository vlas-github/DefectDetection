#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import src.utils.config.config as config

"""
    Модуль для логирования работы программы
"""

# TODO: Проверить значения по умолчанию


info_log_file = config.get_property('log', 'info_log_file', '../../../logs/info.log')
error_log_file = config.get_property('log', 'error_log_file', '../../../logs/error.log')
loging = bool(config.get_property('log', 'loging', 'true'))

if loging:
    info_log = logging.basicConfig(filename=info_log_file, level=logging.INFO,
                                   format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    error_log = logging.basicConfig(filename=error_log_file, level=logging.ERROR,
                                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


def info_log(message):
    if loging:
        info_log.info(message)
    else:
        print message


def debug_log(message):
    if loging:
        info_log.debug(message)
    else:
        print message


def warn_log(message):
    if loging:
        info_log.warning(message)
    else:
        print message


def err_log(message):
    if loging:
        error_log.error(message)
    else:
        print message
