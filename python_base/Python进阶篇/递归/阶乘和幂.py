#!/usr/bin/python
# -*- coding:UTF-8 -*-

"""
1的阶乘是1
n的阶乘是n*(n-1)
"""


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


"""
计算幂：
就像内置函数pow()或者 ** 所做的那样
对于任何数字x，power(x, 0) 都为1
n > 1时，power(x, n) 为power(x, n - 1)与x的乘积
"""


def power(x, n):
    if n == 0:
        return 1
    else:
        return n * power(x, n - 1)
