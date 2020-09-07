# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: MemberVisibility
# @Discription: 成员可见性
# @Author: 子辰
# @Date: 2020-09-06 14:01
# @Software: PyCharm

###############################################
# 成员可见性
#       1. 公开性（外部可以访问相关变量或外部可以调用相关方法）
#       2. 私有性（外部不可以访问相关变量或外部不可以调用相关方法）
###############################################

class Men():
    gender = 'girl'                                # 类变量
    avg_height = 1.66

    def __init__(self, name, age):                  # 构造函数
        self.name = name                            # 实例变量
        """ 在变量前面加两个下横线，就会将变量变成私有变量 """
        self.__age = age
        self.salary = 0

    ''' 2）. 在类中创建方法来修改实例变量的值，推介 '''
    def modify_salary(self, salary):
        self.salary = salary

    def sleep(self):                                # 方法/行为
        print('sleeping')

    def __think(self):
        """ 在方法前面加两个下横线，就会将方法变成私有方法 """
        print('thinking')

    @classmethod                                    # 类方法
    def modify_height(cls, height):
        cls.avgheight += height                     # 改变类的属性
        print('Success. Now the avg_height is ' + str(cls.avg_height))

    @staticmethod                                   # 静态方法
    def plus_num(x, y):                             # 静态方法与普通方法没有区别，因此没有类似于self,cls等约定俗成的东西
        return x * y


# 如果想修改实例变量salary的值，该如何操作？
#   1. 使用Man来修改
#   2. 在类中定义方法来修改
men = Men('lemon', 21)
''' 1）. 从外部使用Men()来修改，确实可以实现，但是不推介 '''
men.salary = 18
print(men.__dict__)
''' 2）. 在类中创建方法来修改实例变量的值，推介 '''
men.modify_salary(19)
print(men.__dict__)