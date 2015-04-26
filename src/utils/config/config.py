#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ConfigParser

"""
    Обертка для конфигов
"""

# TODO: -


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
    except ConfigParser.NoSectionError:
        config.add_section(section)
        set_property(section, option, value)
    except Exception:
        pass


def save_config():
    try:
        config.write(open(config_file, 'wb'))
    except Exception:
        pass


if __name__ == '__main__':
    print get_property('log', 'info_log_file', 'test')
    print get_property('test', 'test-test-test', 'test')
    set_property('test', 'test-test-test', 'test-test-test')
    print get_property('test', 'test-test-test', 'test')
    save_config()