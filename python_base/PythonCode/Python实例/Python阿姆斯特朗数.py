#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
如果一个n位正整数等于其各位数字的n次方之和，则称该数字为阿姆斯特朗数。例如 1^3 + 5^3 + 3^3 = 153。
"""

num = int(input("请输入一个数字："))
sum = 0
n = len(str(num))

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if __name__ == '__main__':
    if num == sum:
        print(num, '是阿姆斯特朗数')
    else:
        print(num, '不是阿姆斯特朗数')
