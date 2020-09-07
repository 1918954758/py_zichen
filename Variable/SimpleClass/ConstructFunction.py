# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: ConstructFunction
# @Discription: 构造函数 & 实例方法
# @Author: 子辰
# @Date: 2020-09-06 12:58
# @Software: PyCharm

#################################################
# 类时一个模板，通过类实例化，可以生成一个或者多个对象
# 类描述具有相同的特征和行为的对象的集合
#################################################
class Human():
    gender = '男'  # 类变量   刻画类本身的特征
    avg_height = 1.7

    def __init__(self, name, age):  # 构造函数
        print('this is __init__')
        # 初始化对象
        # 实例变量，保存了对象的特征
        self.name = name  # 实例变量     保存对象的具体特征
        self.age = age

    def sleep(self):
        print('sleeping')

    def think(self):
        print('thinking')


human = Human('lemon', 21)  # python会将传入的参数保存到对应的参数中，即self.name和self.age中
# 有因为self指向的是实例化后对象本身，也就是会将实参保存到实例化后的对象本身中
# 此时我们可以访问这个实例化对象的属性，name和age
print(human.name)
print(human.age)
# 我们可以使用 __dict__这个方法查看对象中到底是个啥
print(human.__dict__)


#################################################
# 通过实例方法访问实例变量和类变量
#################################################
print("-------------------------------------------------------")
class Man():
    gender = 'male'  # 类变量
    avg_height = 1.7

    def __init__(self, name, age):
        # 初始化对象的特征
        self.name = name
        self.age = age

    def sleep(self):
        print('sleeping')

    def think(self):
        print('thinking')

    def find(self):
        print('this is ' + str(self.name))
        print('this is ' + str(self.age))
        # 1. 利用self关键字和方法 __class__来访问： self.__class__.类变量
        print(self.__class__.gender)
        # 2. 利用类名来访问： Man.类变量
        print(Man.gender)
        # 3. 利用self关键字直接访问类变量： self.类变量
        print(self.gender)
man = Man('lemon', 21)
man.find()
# 在实例方法中访问类变量，方法有三：
#   1. 利用self关键字和方法 __class__来访问： self.__class__.类变量
#   2. 利用类名来访问： Man.类变量
#   3. 利用self关键字直接访问类变量： self.类变量
