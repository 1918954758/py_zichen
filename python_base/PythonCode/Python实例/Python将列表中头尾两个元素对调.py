#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
定义一个列表，并将列表中的头尾两个元素对调。
"""


def reverList():
    arr = input("请输入列表(字符之间用逗号分隔)：").split(",")
    arr1 = arr.copy()
    arr1[0] = arr[len(arr) - 1]
    arr1[len(arr) - 1] = arr[0]
    return arr, arr1


if __name__ == '__main__':
    tup = reverList()
    print(f"{tup[0]} \n{tup[1]}")
