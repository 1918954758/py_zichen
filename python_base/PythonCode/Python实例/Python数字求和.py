#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 用户输入
num1 = input("请输入第一个数字：")
num2 = input("请输入第二个数字：")

sum = float(num1) + float(num2)

if __name__ == '__main__':
    print("数字{0} 和 {1} 相加结果为：{2}".format(num1, num2, sum))
