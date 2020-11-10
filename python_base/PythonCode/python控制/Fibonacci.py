#!/usr/bin/python
# -*- coding: UTF-8 -*-

a, b = 0, 1


def fab(n):
    if n < 1:
        print("输入错误")
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab(n - 1) + fab(n - 2)


if __name__ == "__main__":
    while a < 10:
        print(b, end=',')
        a, b = b, a + b
    print(" ")
    print(fab(10))
