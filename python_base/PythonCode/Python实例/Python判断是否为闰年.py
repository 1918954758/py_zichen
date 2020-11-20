#!/usr/bin/python
# -*- coding: UTF-8 -*-

def yearOfNumber():
    while True:
        try:
            num = int(input("请输入一个年份："))
            if 100 <= num <= 9999:
                return num
            else:
                print("输入的年份不合法，请重新输入！")
                continue
        except ValueError:
            print("输入的年份不合法，请重新输入！")
            continue

def isRunNian(yearN):
    if yearN % 4 == 0:
        if yearN % 100 == 0:
            if yearN % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == '__main__':
    num = yearOfNumber()
    if isRunNian(num):
        print("{}是闰年".format(num))
    else:
        print("{}不是闰年".format(num))
