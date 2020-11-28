#!/usr/bin/python
# -*- coding: UTF-8 -*-


def listMax(li):
    temp = li[0]
    index = 0
    while True:
        if temp <= li[index]:
            temp = li[index]
        index += 1
        if index == len(li):
            break
    return temp


if __name__ == '__main__':
    li = [3, 2, 5, 8, 9, 7, 0, 8, 3, -1, 7, 10]
    print(listMax(li))
    # max()
    print(max(li))
    # sort()
    li.sort()
    print(*li[len(li)-1:])
