#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cmath

# 负数和复数的平方根可以使用以下方法
num1 = int(input("请输入一个数字："))
num_sqrt1 = cmath.sqrt(num1)
if __name__ == '__main__':
    print(num_sqrt1)  # 复数
    print(num_sqrt1.real)  # 实部
    print(num_sqrt1.imag)  # 虚部
    print("{0}的平方根为 {1:0.3f}+{2:0.3f}j".format(num1, num_sqrt1.real, num_sqrt1.imag))
    # print("{0}的平方根为 {1::0.3f}+{2:0.3f}j".format(num1, num_sqrt1.real, num_sqrt1.imag))
