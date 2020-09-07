# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: VariableScope
# @Discription: 变量的作用域
# @Author: 子辰
# @Date: 2020-09-06 00:19
# @Software: PyCharm

####################################################
# python 有哪些作用域：
# 1. L      Local       局部作用域
# 2. E      Enclosing   嵌套函数外层非全局作用域
# 3. G      Global      全局作用域
# 4. B      Built-in    内建作用域
####################################################
"""
变量更具作用域的不同可以分为：  全局变量、局部变量
1. 全局变量：自己编写的整个程序内
2. 局部变量：自己编写的整个函数内
"""
lemon = 5           # 全局作用域
def fruits():
    lemon = 20      # 局部变量
    print(lemon)

""" 变量的引用 """
'''在函数的内部是可以引用全局变量的'''
lemon1 = 5           # 全局作用域
def fruits():
    lemon2 = 20      # 局部变量
    print(lemon2)
    print(lemon1)
''' 在函数的外部是不可以引用局部变量的'''
def fruits():
    lemon2 = 20      # 局部变量
# print(lemon2)  这里引用局部变量会编译不通过
""" 从外部可以引用if,for,while代码块中的变量 """
if 5 > 0:
    lemon = 5
print('if条件块中的变量可以被外部引用：' + str(lemon))
for i in range(0, 10, 1):
    if i == 8:
        lemon = i
        break
print('for循环块中的变量可以被外部引用：' + str(lemon1))
ran = 1
while ran < 3:
    lemon2 = ran
    ran += 1
print('while循环块中的变量可以被外部引用：' + str(lemon2))