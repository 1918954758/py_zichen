#!/usr/bin/python
# -*- coding: UTF-8 -*-

def listMin(li):
    # lis = list(li[:])
    temp = li[0]
    count = 0
    while True:
        if temp >= li[count]:
            temp = li[count]
        count += 1
        if count == len(li):
            break
    return temp


if __name__ == '__main__':
    li = [3, 2, 5, 8, 4, 7, 0, 8, 3, -1, 7]
    print(listMin(li))
    # min()
    print(min(li))
