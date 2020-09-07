# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: AccessEverything
# @Discription: Python中没有什么是不可以访问的
# @Author: 子辰
# @Date: 2020-09-06 14:22
# @Software: PyCharm

#################################################
# 没有什么是不可以访问的
#################################################
class Men():
    gender = 'girl'  # 类变量
    avg_height = 1.66

    def __init__(self, name, age):  # 构造函数
        self.name = name  # 实例变量
        """ 在变量前面加两个下横线，就会将变量变成私有变量 """
        self.__age = age
        self.salary = 0

    ''' 2）. 在类中创建方法来修改实例变量的值，推介 '''

    def modify_salary(self, salary):
        self.salary = salary

    def sleep(self):  # 方法/行为
        print('sleeping')

    def __think(self):
        """ 在方法前面加两个下横线，就会将方法变成私有方法 """
        print('thinking')

    @classmethod  # 类方法
    def modify_height(cls, height):
        cls.avgheight += height  # 改变类的属性
        print('Success. Now the avg_height is ' + str(cls.avg_height))

    @staticmethod  # 静态方法
    def plus_num(x, y):  # 静态方法与普通方法没有区别，因此没有类似于self,cls等约定俗成的东西
        return x * y


# 实例化Men()类
men = Men('lemon', 21)
print(men.__dict__)
# 查看men对象，发现多了一个 '_Men__age':21
# {'name': 'lemon', '_Men__age': 21, 'salary': 0}
# 这样我们就可以根据给出的名字取访问私有变量
print(men._Men__age)  # 这样也可以访问私有变量age了
# 私有方法和私有变量差不多
print(men._Men__think())
