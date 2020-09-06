# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: ClassFunction
# @Discription: 类方法
# @Author: 子辰
# @Date: 2020-09-06 13:35
# @Software: PyCharm

#################################################
# 类方法
#################################################
class Man():
    gender = 'male'
    avg_height = 1.7
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sleep(self):
        print('sleeping')
    def think(self):
        print('thinking')

    @classmethod
    def modify_height(cls, height):
        cls.avg_height += height
        print('Success. Now the avg_height is ' + str(cls.avg_height))
Man.modify_height(0.05)
# 查看类的属性
print(Man.__dict__)























