#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    _list_ = [x * y for x in range(1, 5) if x > 2 for y in range(1, 4) if y < 3]
    print(_list_)

# 执行顺序
if __name__ == '__main__':
    z = []
    for x in range(1, 5):
        if x > 2:
            for y in range(1, 4):
                if y < 3:
                    z.append(x * y)
    print(z)

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
if __name__ == '__main__':
    __list__ = [[row[i] for row in matrix] for i in range(4)]
    print(__list__)
# 执行顺序
if __name__ == '__main__':
    l1 = []
    for i in range(4):
        l2 = []
        for row in matrix:
            l2.append(row[i])
        l1.append(l2)
    print(l1)
