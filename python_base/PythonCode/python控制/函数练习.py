#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 计算最大值(不定长参数)
def max1(*args):
    # tuple = (2, 3, 5, 7, 3, 6)
    tup = args
    len1 = len(tup)
    tmp = 0
    for i in range(0, len1, 1):
        if tup[i] > tmp:
            tmp = tup[i]
        else:
            tmp = tmp
    return tmp


# if __name__ == '__main__':
# print(max1(1, 3, 5, 11, 3, 8, 5, 98, 4, 9, 8))

# 传递不同的参数(必须参数， 关键字参数， (/, c, d)位置参数或关键字参数, (*, e, f)关键字参数)
def f(a, b, /, c, d, *, e, f):
    sum = a + b - c + d - e + f
    return sum


'''
if __name__ == '__main__':
    result1 = f(5, 3, 6, 2, e=4, f=2)
    print(result1)
    result2 = f(5, 3, c=6, d=2, e=4, f=2)
    print(result2)
'''


# 默认值参数
def defaultargs(a, b="子辰"):
    sum = a + b
    return sum


if __name__ == '__main__':
    result3 = defaultargs("python3", b="不太好学呀！")
    print(result3)
