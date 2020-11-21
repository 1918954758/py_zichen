#!/usr/bin/python
# -*- coding: UTF-8 -*-

a = float(input("输入三角形第一边长："))
b = float(input("输入三角形第二边长："))
c = float(input("输入三角形第三边长："))

while a + b < c or a + c < b or b + c < a:
    print("三条边不可以构成三角形，请重新输入！！")
    a = float(input("输入三角形第一边长："))
    b = float(input("输入三角形第二边长："))
    c = float(input("输入三角形第三边长："))
s = (a + b + c) / 2

area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

if __name__ == '__main__':
    print("三角形面积为 %0.2f" % area)
