#!/usr/bin/python
# -*- coding: UTF-8 -*-

num = float(input("输入一个数字："))

if __name__ == "__main__":
    if num > 0:
        print(num, "整数")
    elif num == 0:
        print(num, "0")
    else:
        print(num, "负数")
