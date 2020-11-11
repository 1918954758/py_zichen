#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys


class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

if __name__ == '__main__':
    while True:
        i = next(myiter)
        print(i)
        if i > 99:
            sys.exit()
