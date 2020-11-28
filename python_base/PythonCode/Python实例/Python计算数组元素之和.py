#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
输入 : arr[] = {1, 2, 3}

输出 : 6

计算: 1 + 2 + 3 = 6
"""


def sumarr():
    arr = [1, 2, 3]
    index = len(arr)
    sum = 0
    for x in range(0, index):
        sum += arr[x]
    return sum


if __name__ == "__main__":
    print(sumarr())
