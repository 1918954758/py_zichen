#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 以下函数在fab中直接打印，会导致代码复用性较差
from pip._vendor.msgpack.fallback import xrange


def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    fab(5)


# 使函数返回一个list，提高代码复用性，但是这样会随着参数max的增大运行中占用的内存会增大，也不是最优选择
def fab1(max):
    n, a, b = 0, 0, 1
    L = []
    while n < max:
        L.append(b)
        a, b = b, a + b
        n += 1
    return L


if __name__ == '__main__':
    fab1(5)


# 要想解决内存占用大的问题，我们需要使用iterable对象来迭代
# 这样在每次迭代中返回下一个数值，内存空间占用很小。因为xrange不返回list，而是返回iterable对象。
def fab2(max):
    n, a, b = 0, 0, 1
    for i in xrange(1000):
        return i


if __name__ == '__main__':
    fab2(5)


# 利用iterable我们把fab函数改写为一个支持iterable的class，以下是滴三个版本的fab：
class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):  # python3中使用 __next__(self)  # python2中使用 next(self)
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        else:
            raise StopIteration()


if __name__ == '__main__':
    for n in Fab(5):
        print(n)


# 如上似乎可以满足要求了，但是代码并不简洁
# 要想也使代简洁，同时又要获得iterable的效果那么我们就可以使用yield了
def Fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 使用yield
        # print
        a, b = b, a + b
        n += 1


if __name__ == '__main__':
    for n in Fab1(5):
        print(n)
