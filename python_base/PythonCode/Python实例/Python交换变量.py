#!/usr/bin/python
# -*- coding: UTF-8 -*-

x1 = input("输入x值：")
y1 = input("输入y值：")

temp = x1
x2 = y1
y2 = temp

if __name__ == '__main__':
    print("{0} <===> {1}".format(x1, y1))
    print("{0} <===> {1}".format(x2, y2))

if __name__ == '__main__':
    a1 = 1
    b1 = 2
    a2, b2 = b1, a1
    print(a1, b1)
    print(a2, b2)
