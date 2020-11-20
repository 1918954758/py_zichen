#!/usr/bin/python
# -*- coding: UTF-8 -*-

def isNum():
    while True:
        try:
            num = int(input("请输入一个数字："))
            return num
        except ValueError:
            print("输入的内容不合法，请重新输入：")
            continue


if __name__ == '__main__':
    number = isNum()
    if number % 2 == 0:
        print("{}是偶数".format(number))
    else:
        print("{}是奇数".format(number))
