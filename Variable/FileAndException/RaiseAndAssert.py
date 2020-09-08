# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: RaiseAndAssert
# @Discription: raise 和 assert
# @Author: 子辰
# @Date: 2020-09-08 22:23
# @Software: PyCharm
################################################
# raise 和 assert
################################################

"""
raise 抛出异常
    除了可以使用try来捕获异常，我们还可以使用raise来显式地引发异常，一旦引发异常，程序将终止
assert  断言
    assert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言，并更好的知道是哪里出了问题。
    assert表示是基本格式：
        assert expression [, arguments]
    如果bool_expression 为False，则会抛出arguments这个自定义异常信息
    如果bool_expression 为True，则不会抛出arguments这个自定义的异常信息
"""
'''
需求1：
    1. 传入一个参数，判断是否为整型类型，如果不是，则抛出异常，终止程序。
    2. 判断是否大于等于5，如果小于5，则抛出异常，终止程序。
'''

def f1(num):
    if not isinstance(num, int):
        raise Exception('该参数不是一个整型类型')
    if num < 5:
        raise Exception('该参数小于5')

def f3(num):
    assert isinstance(num, int), '该参数不是一个整型'
    assert num >= 5, '该参数小于5'               # 这个语句有意思，如果assert后面的条件成立，则不会抛出，不成立才会抛出

'''
需求2：
    传入若干个参数，判断参数个数，如果小于等于5，则抛出异常，终止程序
'''
def f2(*args):
    if len(args) <= 5:
        raise Exception('该参数个数小于等于5')

def f4(*args):
    assert len(args) > 5, '该参数的个数小于等于5'



if __name__ == '__main__':
    # f2(1, 2, 3, 4, 5, 6)
    f4(1, 2, 3, 5, 6, 8, 1)
