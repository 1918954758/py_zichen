#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

phone = '2004-959-559 # 这是一个电话号码'

# 移除注释
num = re.sub(r'#.*', "", phone)

if __name__ == '__main__':
    print("电话号码 ： ", num)

# 替换非数字部分
num = re.sub(r'\D', ' ', phone)

if __name__ == '__main__':
    print("电话号码 ： ", num)
    print("电话号码 ： ", re.sub(r'\D', '', phone))
