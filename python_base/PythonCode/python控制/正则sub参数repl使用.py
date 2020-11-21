#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re


# 将匹配的数字乘2

def double(obj):
    value = int(obj.group("value"))
    return str(value * 2)


def double1(obj):
    value1 = obj.group("value1")
    return value1 * 2


s = 'A23G34G32FDSAF43DV23R'
if __name__ == '__main__':
    print(re.sub('(?P<value>\d+)', double, s))
    print(re.sub('(?P<value1>\D)', double1, s))
