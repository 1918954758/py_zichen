#!/usr/bin/python
# -*- coding: UTF-8 -*-
from functools import reduce

if __name__ == '__main__':
    s = 'zichen'
    # 逆序输出
    print(s[::-1])
    # 使用函数reversed()
    print(''.join(reversed(s)))
    # reduce + lambda 反转
    print(reduce(lambda x, y: y + x, s))
