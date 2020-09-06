# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Extends
# @Discription: 继承
# @Author: 子辰
# @Date: 2020-09-06 14:34
# @Software: PyCharm
#################################################
# 继承
#################################################

"""
需求：
现在需要创建一个ChineseMen类，要求，这个类要与Men类的特征和行为相同
"""
class Men():            # 父类或者基类
    genger = 'girl'
    avg_height = 1.7

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('父类构造函数被执行了')

    def sleep(self):
         print('父类的sleep()方法被执行了')

    def think(self):
        print('thinking')

class ChineseMen(Men):          # 子类，，，，，，继承父类  Men
    pass

lemon = ChineseMen('lemon', 21)
print(lemon.__dict__)           # output ---->  {'name': 'lemon', 'age': 21}
lemon.sleep()                   # output ---->  sleeping
# print(lemon._ChineseMen__age)   子类是不可以访问父类的私有成员的


# 扩展
# 1. 除了想保存具体对象的姓名，年龄，还想保存对象的身高
# 2. sleep方法，更改为 print(self.name + ' is sleeping')
# 需要在子类中重写构造函数
print("-----------------------------------------------------------")
class ChineseMen2(Men):
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def sleep(self):
        print(self.name + ' is sleeping')

lemon2 = ChineseMen2('lemon2', 21, 166)
print(lemon2.__dict__)

# 此外，我们还可以通过将实参传递给父类，来实现保存
print("-----------------------------------------------------------")
class ChineseMen3(Men):
    def __init__(self, name, age, height):
        # Men.__init__(self, name, age)   # 除这种调用之外，我们习惯用super关键字来调用父类的方法
        super(ChineseMen3, self).__init__(name, age)
        self.height = height
        print('子类构造函数被执行了')

    def sleep(self):
        # Men.sleep(self)                 # 除这种调用之外，我们习惯用super关键字来调用父类的方法
        super(ChineseMen3, self).sleep()
        print(self.name + ' 子类sleep()方法被执行了')

lemon3 = ChineseMen3('lemon3', 21, 166)
print(lemon3.__dict__)
print(lemon3.sleep())
print('-----------------------------------------------------------')
def add(name, age):
    mne2 = Men(name, age)
    print(mne2.name)
add('lemon5', 21)

"""
注意：
1. 父类必须要写在子类的前面，如果写在后面，编译不通过
2. 子类可以继承多个父类，中间用英文逗号链接
"""