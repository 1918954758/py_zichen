# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: UseRetuen
# @Discription: 函数return的用法
# @Author: 子辰
# @Date: 2020-09-06 01:10
# @Software: PyCharm

###################################
# 程序运行第一个return语句后，大多情况下，会跳出该函数，不会执行之后的代码
###################################
def test():
    a = 1
    return print(a)
    print(a)
test()

###################################
# 函数内，可存在多个return，一般与if条件搭配使用
###################################
print("----------------------------------------------------------")
def test1(x, y):
    if x > y:
        return print(x)
    elif x < y:
        return print(y)
    else:
        return print(x + y)
test1(3, 3)
###################################
# return 支持返回多个结果
###################################
print("----------------------------------------------------------")
def fruits(lemon, apple):
    lemon = lemon + 2
    apple = apple + 1
    return print(lemon, apple)
fruits(5, 8)
