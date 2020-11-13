#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

lis = [1, 2, 3, 4]
it = iter(lis)

if __name__ == '__main__':
    for x in it:
        print(x, end=" ")
if __name__ == '__main__':
    while True:
        try:
            # print(it, end=" ")
            print(next(it), end=" ")
        except StopIteration:
            sys.exit()
