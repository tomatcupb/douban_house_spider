# -*- coding: utf-8 -*-
# module util
import time
import hashlib
import sys

sys.path.append('/home/hadoop/spiders')


def get_md5(str):
    m5 = hashlib.md5()
    m5.update(str)
    md5 = m5.hexdigest()
    return md5


def now_time(format='%Y-%m-%d %H:%M:%S'):
    return time.strftime(format, time.localtime())
