#!/usr/bin/python
# -*- coding: UTF-8 -*-

def fibo(num):
    if num <= 1:
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)


if __name__ == '__main__':
    num = int(input("请输入一个数："))
    if num < 0:
        print("请输入正数")
    else:
        for x in range(num):
            print(fibo(x))
