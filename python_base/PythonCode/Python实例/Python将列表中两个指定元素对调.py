#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
定义一个列表，并将列表中的指定位置的两个元素对调。

例如，对调第一个和第三个元素：

对调前 : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
对调后 : [19, 65, 23, 90]
"""


def swapPosition():
    arr = input("请输入列表(字符之间用逗号分隔)：").split(",")
    position = input("请输入对调的两个元素的位置：").split(",")
    if int(position[0]) < 0 or int(position[1]) < 0:
        raise ValueError("起始位置坐标输入有误！！！")
    if int(position[0]) >= len(arr) or int(position[1]) >= len(arr):
        raise ValueError("末尾位置坐标输入有误！！！")
    # arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # position = [3, 5]
    arr1 = arr.copy()
    arr1[int(position[0]) - 1] = arr[int(position[1]) - 1]
    arr1[int(position[1]) - 1] = arr[int(position[0]) - 1]
    return arr, arr1


if __name__ == "__main__":
    result = swapPosition()
    print(f"{result[0]} \n{result[1]}")
