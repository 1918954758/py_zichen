# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: ScopeChain
# @Discription: python作用域链
# @Author: 子辰
# @Date: 2020-09-06 00:52
# @Software: PyCharm

####################################################
# 作用域链：作用域具有链式查找特性
# 特点：
# 1. 函数内部引用变量，会优先引用最近局部变量
# 2. 函数内部引用变量，会逐级向上寻找
####################################################

lemon = 10
def fruits():
    lemon = 5
    print(lemon)
fruits()
# 该函数，会先找函数内部的变量，如果找不到，会取找全局变量

