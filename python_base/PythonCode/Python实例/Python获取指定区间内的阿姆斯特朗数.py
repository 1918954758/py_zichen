#!/usr/bin/python
# -*- coding: UTF-8 -*-

lis = []


def getAMSTLS(nummin, nummax):
    for i in range(nummin, nummax + 1):
        sum = 0
        n = len(str(i))
        temp = i
        while temp > 0:  # 一个数一个数地处理阿姆斯特朗数
            digit = temp % 10
            sum += digit ** n
            temp //= 10
        if i == sum:
            lis.append(i)
    return lis


if __name__ == '__main__':
    nummin = int(input("请输入一个最小值："))
    nummax = int(input("请输入一个最大值："))
    lis = getAMSTLS(nummin, nummax)
    print(lis)
