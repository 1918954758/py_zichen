# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: StaticMethod
# @Discription: 静态方法
# @Author: 子辰
# @Date: 2020-09-06 13:49
# @Software: PyCharm

class Men():
    gender = 'girl'                                # 类变量
    avg_height = 1.66

    def __init__(self, name, age):                  # 构造函数
        self.name = name                            # 实例变量
        self.age = age

    def sleep(self):                                # 方法/行为
        print('sleeping')

    def think(self):
        print('thinking')

    @classmethod                                    # 类方法
    def modify_height(cls, height):
        cls.avgheight += height                     # 改变类的属性
        print('Success. Now the avg_height is ' + str(cls.avg_height))

    @staticmethod                                   # 静态方法
    def plus_num(x, y):                             # 静态方法与普通方法没有区别，因此没有类似于self,cls等约定俗成的东西
        return x * y

#################################################
# 静态方法
# 静态方法与普通方法美哦与什么区别
# 静态方法与类、对象没有太大关系的时候，可以使用该方法
#################################################
''' 调用静态方法 '''
man = Men('lemon', 21)
ret = man.plus_num(2, 3)
print(ret)
