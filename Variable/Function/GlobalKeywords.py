# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: GlobalKeywords
# @Discription: Global关键字
# @Author: 子辰
# @Date: 2020-09-06 00:58
# @Software: PyCharm

#####################################################
# 函数外部，一般情况下，不可以引用局部变量
# 如果我们使用Global这个关键字，情况则会不一样
#####################################################
def fruits():
    global lemon  # 使用global关键字申明lemon变量为全局变量
    global pear, apple, banana  # 使用global可以申明多个变量为全局变量
    lemon = 5
fruits()
print(lemon)

"""
global是否可以给全局变量赋值呢？
"""
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
banana = 5
def fruit():
    banana = 10
    print('局部的banana为：' + str(banana))
fruit()
print('全局的banana为：' + str(banana))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
def fruit():
    global banana
    banana = 10
    print('局部的banana为：' + str(banana))
fruit()
print('全局的banana为：' + str(banana))