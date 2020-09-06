# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: SimpleClass
# @Discription: 创建简单的类
# @Author: 子辰
# @Date: 2020-09-06 12:11
# @Software: PyCharm

###############################################
# 类：是描述具有相同特征和行为的对象的集合
# 通过变量，刻画类的特征
# 通过方法，刻画类的行为
#
# class 类名():
#       变量   # 刻画类的特征
#       def 相关方法(self, 相关参数):
#           pass
###############################################

""" simple class """


class Human():
    gender = '男'
    avg_height = 1.7

    def think(self):
        print('thinking')

    def sleep(self):
        print('sleep')


# 类的实例化
human = Human()

"""
对于self说明：
    1. self名称是约定俗成的
    2. self指向的是类实例化后的对象本身
    3. self只有在类的方法中才会有，函数是不必带有self的
    4. self在调用时不必传入相应的参数。
"""
'''
调用类中的方法
在调用类中的方法时，不必手动传入self这个参数，python会自动帮我们传入
'''
human.think()
human.sleep()
