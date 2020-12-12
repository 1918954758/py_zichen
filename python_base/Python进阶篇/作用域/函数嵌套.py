#!/usr/bin/python
# -*- coding:UTF-8 -*-


"""嵌套函数，类似以下嵌套以及外层函数返回内层函数的嵌套，叫做闭包"""


def a(x):
    def b(y):
        return x * y

    return b


"""我们可以使用 nonlocal 给外部函数的变量赋值"""


if __name__ == '__main__':
    i = a(4)
    print(i(6))
    print(a(5)(2))
