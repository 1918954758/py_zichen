#!/usr/bin/python
# -*- coding:UTF-8 -*-

def shellSort(arr):
    n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap = int(gap / 2)
    return arr


if __name__ == '__main__':
    arr = [12, 34, 54, 2, 3]
    n = len(arr)
    print("排序前:")
    print(arr)
    print("\n排序后:")
    print(shellSort(arr))
