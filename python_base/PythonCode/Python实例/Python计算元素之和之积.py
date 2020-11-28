#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
计算列表元素之和之积
"""

"""利用循环遍历"""


# 求和
def sum1(args):
    list1 = list(args[:])
    sum = 0
    for n in range(0, len(list1)):
        sum += list1[n]
    return sum


# 求积
def product1(args):
    list1 = list(args[:])
    product = 1
    for n in range(0, len(list1)):
        if list1[n] != 0:
            product *= list1[n]
        else:
            product = 0
    return product


if __name__ == '__main__':
    li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"求和：{sum1(li)}")
    print(f"求积：{product1(li)}")
