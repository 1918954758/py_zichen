#!/usr/bin/python
# -*- coding: UTF-8 -*-

import random

if __name__ == '__main__':
    print("从range(100)返回一个随机数：", random.choice(range(100)))
    print("randrange(1, 100, 2)：", random.randrange(1, 100, 2))
    print("random()：", random.random())
    random.seed()
    print("使用默认种子生成随机数：", random.random())
    random.seed(10)
    print("使用整数10种子生成随机数：", random.random())
    random.seed(10)
    print("使用整数10种子生成随机数：", random.random())
    random.seed("hello", 2)
    print("使用字符串种子生成随机数：", random.random())
    list = [20, 16, 10, 5]
    random.shuffle(list)
    print("随机排序列表：", list)
    random.shuffle(list)
    print("随机排序列表：", list)
    print("uniform(5, 10)的随机浮点数：", random.uniform(5, 10))
    print("uniform(7, 14)的随机浮点数：", random.uniform(7, 14))
