#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self.a

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):            # 可以像list一样使用方括号取值
        a, b = 1, 1
        for n in range(item):
            a, b = b, a + b
        return a


fib = Fib()

if __name__ == '__main__':
    print(fib[3])
    print(fib[8])
