#!/usr/bin/env python
# -*- coding: utf-8 -*-


import ConfigParser
import argparse

"""
    Обертка для конфигов
"""

# TODO: Нормальные пути


project_path = '/home/vlasov-id-131216/Dropbox/Универ/Диплом/project/DefectDetection/'
config_file = project_path + 'defaults.cfg'
config = ConfigParser.ConfigParser()
config.readfp(open(config_file))


def full_path(path):
    return project_path + path


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


def load_config(fn):
    """
    Декоратор для подгрузки исходных, не переданных через командную строку, из конфигов данных для запуска приложения
    :param fn: Функция для которой нужны подкрузить аргументы
    :return: Функция обернутая в декоратор
    """
    def wrapped(args):
        if args.area is None:
            args.area = map(lambda x: int(x),
                            get_property('work', 'area').replace('[', '').replace(']', '').split(', '))
        if args.point is None:
            args.point = map(lambda x: int(x),
                             get_property('work', 'point').replace('[', '').replace(']', '').split(', '))
        if args.size is None:
            args.size = map(lambda x: float(x),
                            get_property('work', 'size').replace('[', '').replace(']', '').split(', '))
        if args.type is None:
            args.type = int(get_property('work', 'type'))
        fn(args)

    return wrapped


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--area',  help='work area (-a x1 y1 x2 y2)',  nargs='+', type=int)
    parser.add_argument('-p', '--point', help='point (-p x y)',              nargs='+', type=int)
    parser.add_argument('-s', '--size',  help='image size in mm (-i h w)',   nargs='+', type=float)
    parser.add_argument('-t', '--type',  help='1 - perpendicular; 2 - area; 0 - both',  type=int)
    _args = parser.parse_args()

    set_property('work', 'area', _args.area)
    set_property('work', 'point', _args.point)
    set_property('work', 'size', _args.size)
    set_property('work', 'type', _args.type)
    save_config()
