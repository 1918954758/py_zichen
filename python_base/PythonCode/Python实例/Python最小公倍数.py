#!/usr/bin/python
# -*- coding: UTF-8 -*-

def lcm(x, y):
    if x > y:
        temp = x
    else:
        temp = y
    while True:
        if temp % x == 0 and temp % y == 0:
            return temp
        temp += 1


if __name__ == '__main__':
    num1 = int(input("请输入一个数："))
    num2 = int(input("请输入另一个数："))
    print("{}和{}的最小公倍数为：{}".format(num1, num2, lcm(num1, num2)))
