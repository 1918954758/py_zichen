#!/usr/bin/python
# -*- coding: UTF-8 -*-

list = [1, 2, 3, 4, 7, 5, 9, 3, 5, 2, 3, 6, 2, 8, 4, 5, 7, 4, 5, 9, 5, 0, 4, 6, 3, 2, 5, 7, 8, 4, 6, 3, 0, 0, 3, 5, 6]
seq = ['a', 'b', 'c', 'd']

if __name__ == '__main__':
    print(list)
    list.append(3)
    print(list)
    count = list.count(7)
    print(count)
    list.extend(seq)
    print(list)
    print(list.index(6))
    list.insert(1, 'zichen')
    print(list)
    list.pop()
    print(list)
    list.pop(-2)
    print(list)
    list.remove(2)
    print(list)
    list.reverse()
    print(list)
    # list.sort(key=None, reverse=False)
    # print(list)
    list2 = list.copy()
    print(list2)
    list2.clear()
    print(list2)