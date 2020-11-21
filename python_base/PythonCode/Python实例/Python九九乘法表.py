#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    for i in range(1, 10):
        for j in range(1, i + 1):
            print("{} × {} = {} \t".format(j, i, i * j), end="")
        print()
