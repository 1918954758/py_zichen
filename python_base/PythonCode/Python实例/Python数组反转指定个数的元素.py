#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
定义一个整型数组，并将指定个数的元素翻转到数组的尾部。

例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。

以下演示了将数组的前面两个元素放到数组后面。

原始数组:

    [1, 2, 3, 4, 5, 6, 7]

翻转后：
    [3, 4, 5, 6, 7, 1, 2]

"""


def reverseArr():
    arr = input("请输入列表(字符之间用逗号分隔)：").split(",")
    index = int(input("请输入要反转的角标(角标不可以大于{})：".format(len(arr))))
    if index > len(arr):
        raise ValueError
    arr1 = []
    arr2 = []
    for i in range(0, index):
        arr1.append(arr[i])
    for j in range(index, len(arr)):
        arr2.append(arr[j])
    arr2.extend(arr1)
    return arr2


if __name__ == '__main__':
    print(reverseArr())
