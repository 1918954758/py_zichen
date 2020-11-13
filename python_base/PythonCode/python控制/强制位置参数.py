#!/usr/bin/python
# -*- coding: UTF-8 -*-

def f(a, b, /, c, d, *, e, f):
    sum = a + b + c + d + e + f
    return sum


if __name__ == '__main__':
    print(f(10, 20, 30, 40, e=50, f=60))

if __name__ == '__main__':
    print(f(10, 20, c=30, d=30, e=70, f=100))
