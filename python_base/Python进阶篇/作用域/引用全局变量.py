#!/usr/bin/python
# -*- coding:UTF-8 -*-

parameter = 'Berry'

"""使用同名的参数，不可以使用全局变量"""


def combine1(parameter):
    print(parameter + parameter)


"""使用同名参数，必须告诉python解释器那个参数是全局变量"""


def combine2(parameter):
    print(parameter + globals()['parameter'])


"""也可以使用global关键字声明参数是引用全局变量"""


def combine3(para):
    global parameter
    print(para + parameter)


"""不同命的参数，python在局部作用域中找不到该参数，就回去全局变量中寻找"""


def combine4(para):
    print(para + parameter)


if __name__ == '__main__':
    combine1('Shrub')  # output => ShrubShrub
    combine2('Shrub')  # output => ShrubBerry
    combine3('Shrub')  # output => ShrubBerry
    combine4('Shrub')  # output => ShrubBerry
