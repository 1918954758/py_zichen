# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: FunctionParamType
# @Discription: 函数参数类型
# @Author: 子辰
# @Date: 2020-09-05 21:03
# @Software: PyCharm

"""
def func_name(param1, *args, param2 = 0, **kwargs):
    pass
声名函数时，可以不定义任何形式参数。
声名函数时，如果需要定义形式参数，形式参数类型有：必须参数， 可变参数，默认值参数，可变关键字参数，这四种

定义函数的时候，一般有一下常见形参：
param1          必须参数        （定义了多少个参数，就必须传递多少个参数）
*args           可变参数        （可以传递 大于等于0个参数）
param2 = 0      默认值参数      （给参数赋默认值）
**kwards        可变关键字参数  （可以传递任意个关键字参数）

如果创建一个含有多个类型参数的情况，应该按照 必须参数、可变参数、默认值参数、可变关键子参数的顺序来排列，，不然可能出现意想不到的情况
"""
###############################
# 必须参数
###############################
''' 声名了多少个必须参数，调用的时候就必须传递多少个实参 '''


def add(x, y):
    result = x + y
    return result


add(2, 3)
''' 必须参数如果太多的话，我们可以封装成一个对象来传递 '''
''' 
如果我们调用的时候记不住参数的顺序，该怎么办？
这时候，就可以使用关键字参数，可以告诉python，我们赋值的实参，到底是哪个
'''


def detail(apple, lemon):
    print('apple 有 %s 个' % str(apple))
    print('lemon 有 %s 个' % str(lemon))


detail(apple=10, lemon=21)

''' 使用关键字参数，不需要知道必须参数的顺序 '''

###############################
# 可变参数
###############################
'''
序列解包： 将序列中的元素平铺出来，按照顺序分别赋值给多个变量
这里的序列包括：字符串，列表，元组
'''
''' 序列解包-字符串 '''
print('----------------------序列解包-字符串------------------------')
s = '123'
a, b, c = s
print('a的值为：' + str(a) + '类别为：' + str(type(a)))
print('b的值为：' + str(b) + '类别为：' + str(type(b)))
print('c的值为：' + str(c) + '类别为：' + str(type(c)))
print('----------------------------------------------')
''' 
赋值的变量数量，需要与序列中的元素数量一致 
如果 s = '1234'
a, b, c = s
这种情况就会报错，反正必须一致，不一致就会报错
'''
'''
序列解包-列表
'''
print('----------------------序列解包-列表------------------------')
l = [1, 2, 3]
d, e, f = l
print('d的值为：' + str(d) + '类别为：' + str(type(d)))
print('e的值为：' + str(e) + '类别为：' + str(type(e)))
print('f的值为：' + str(f) + '类别为：' + str(type(f)))
print('----------------------------------------------')
''' 序列解包-元组 '''
print('----------------------序列解包-元组------------------------')
tu = (1, 2, 3)
g, h, i = tu
print('g的值为：' + str(g) + '类别为：' + str(type(g)))
print('h的值为：' + str(h) + '类别为：' + str(type(h)))
print('i的值为：' + str(i) + '类别为：' + str(type(i)))
print('----------------------------------------------')
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
对于可变参数，我们可传递任意个参数，这些参数在函数调用的时候自动组装成一个tuple
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>可变参数学习---start---<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")


def func_args(*args):
    print(args)
    print(type(args))


'''不传参数，默认组装成一个空tuple'''
print(func_args())
'''传入两个参数，默认组装成tuple类型'''
print(func_args(1, 2))
'''传入一个元组，也会把这个元组组装成一个元组的元素来传递'''
a = (1, 2)
print(func_args(a))
'''我么可以用解包的方式，将函数组装成的二维元组，变成一维元组'''
print(func_args(*a))


#  *号的作用是，将参数元组的元素平铺，传递到可变参数的函数里
#  如果你想将一个序列内的元素平铺出来，传递到可变参数的函数里，可以使用序列解包操作

# eg:创建一个函数，用户可传入任意值，并返回任意值相加后的值
def add_all(*args):
    sum = 0
    for i in args:
        sum += i
    return print(sum)
add_all(*(1, 2, 3))
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>可变参数学习---end---<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
###############################
# 默认值参数
###############################
def func_name(param1='default1', param2='default2'):
    pass


'''
默认值参数，指的是，参数在定义时，设置的默认值。
调用函数时，如果需要修改默认值参数，建议使用关键字参数，对默认值参数进行重新赋值。
关键字参数，可以不遵循默认值参数的顺序
'''


def message(name, age, sex='girl', nationality='China'):
    print('我叫：' + str(name))
    print('今年：' + str(age) + '岁')
    print('性别：' + str(sex))
    print('国籍：' + str(nationality))


print('--------------------------------------')
message('lemon', 21)
print('--------------------------------------')
message('Alice', 24, sex='men', nationality='USA')

###############################
# 可变关键字参数
###############################
'''可变关键字参数，可传递任意个关键字参数，这些关键字参数在函数调用的时候会自动组装成为一个dict'''
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>可变关键字参数学习---start---<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
def func_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
# 传入一个空值，可变关键字参数会默认组装成一个空字典
func_kwargs()
# 传入两个值，可变关键字参数会默认组装成一个有两个元素的字典
func_kwargs(lemon = 5, apple = 10)
# 传入一个字典，可变关键字参数会默认将该字典作为一个新字典的元素传入
'''如果我们传入一个字典，则需要在前面加上两个*号，将字典的元素平铺出来，进行传入'''
dic = {'lemon':21, 'apple':10}
func_kwargs(**dic)
''' 这里的 ** 代表将dic 字典中的键值对平铺出来，将每个键值对传递到可变关键字参数的函数里面 '''


print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>可变关键字参数学习---end---<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")