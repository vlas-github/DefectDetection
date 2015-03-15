import os.path
from log import err_log


def args_validator(fn):
    def wrapped(args):
        if (args.mode != 'console' or args.mode != 'gui'):
            err_log('unidentified mode')
        elif (os.path.exists(args.image)):
            err_log('image not found')
        elif (len(args.area) != 4):
            err_log('area format is incorrect')
        elif (len(args.pint) != 2):
            err_log('point format is incorrect')
        elif (len(args.size) != 2):
            err_log('size format is incorrect')
        else:
            fn(args)
    return wrapped