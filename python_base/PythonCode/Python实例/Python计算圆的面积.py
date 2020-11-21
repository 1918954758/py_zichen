#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math


def findArea(r):
    # PI = 3.142
    PI = math.pi
    return PI * (r ** 2)


if __name__ == '__main__':
    print("圆的面积为 %.6f" % findArea(float(input("请输入圆的半径："))))
