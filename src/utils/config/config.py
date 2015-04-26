#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ConfigParser


"""
    Обертка для конфигов
"""


config_file = '../../../defaults.cfg'
config = ConfigParser.ConfigParser()
config.readfp(open(config_file))


def get_property(section, option, default_value=""):
    try:
        return config.get(section, option)
    except Exception:
        return default_value


def set_property(section, option, value):
    try:
        config.set(section, option, value)
        save_config()
    except Exception:
        pass


def save_config():
    config.write(open(config_file, 'wb'))
