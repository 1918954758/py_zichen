#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
定义一个列表，并将它翻转。

例如，对调第一个和第三个元素：

翻转前 : list = [10, 11, 12, 13, 14, 15]
翻转后 : [15, 14, 13, 12, 11, 10]
"""


def reverList():
    arr = input("输入要反转的列表(字符之间用逗号分隔)：").replace(" ", "").split(",")
    arr2 = arr.copy()
    arr2Index = len(arr) - 1
    arr1Index = 0
    while True:
        arr2[arr2Index] = int(arr[arr1Index])
        arr1Index += 1
        arr2Index -= 1
        if arr2Index < 0:
            break
    return arr, arr2


if __name__ == "__main__":
    lis = reverList()
    arr1 = []
    for i in range(0, len(lis[0])):
        arr1.append(int(lis[0][i]))
    print(f"{arr1} \n{lis[1]}")
