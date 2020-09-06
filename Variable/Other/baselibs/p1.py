# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: p1
# @Discription: 
# @Author: 子辰
# @Date: 2020-09-07 00:15
# @Software: PyCharm

def add(x, y):
    sum = x + y
    print(sum)
    return sum
# 代表在当前模块运行，才会执行add(3, 4)
if __name__ == '__main__':
    add(3, 4)