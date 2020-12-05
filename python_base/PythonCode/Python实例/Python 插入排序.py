#!/usr/bin/python
# -*- coding: UTF-8 -*-


def insertDic(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    arr = [1, 2, 3, 2, 3, 7, 8, 3, 7, 4, 7, 2, 6]
    arr1 = []
    insertDic(arr)
    print("排序后的数组:")
    for i in range(len(arr)):
        arr1.append(i)
    print(arr1)
