#!/usr/bin/python
# -*- coding: UTF-8 -*-

def result(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i
    return sum


if __name__ == '__main__':
    print(result(10))
