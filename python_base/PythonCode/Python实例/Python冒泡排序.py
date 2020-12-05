#!/usr/bin/python
# -*- coding:UTF-8 -*-

def sort(arr):
    n = len(arr)

    # 遍历所有数组元素
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11, 2, 65, 23, 12, 76, 48, 79, 35]
    print(sort(arr))
