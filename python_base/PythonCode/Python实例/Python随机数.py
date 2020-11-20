#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

if __name__ == '__main__':
    print(random.randint(0, 9))

'''
产生一个 1 到 10 的随机数：
random.randint(1, 10)
产生一个 0 到 1 的随机浮点数：
random.random()
产生一个 1.1 到 5.4 之间的随机浮点数：
random.uniform(1.1, 5.4)
从序列中随机选取一个元素：
random.choice(' ')
生成从 1 到 100 间隔为 2 的随机整数：
random.randrange(1, 100, 2)
'''
if __name__ == '__main__':
    print(random.randint(1, 10))
    print(random.random())
    print(random.uniform(1.1, 5.4))
    print(random.choice(' '))
    print(random.randrange(0, 100, 2))
