# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: TryCatchFinally
# @Discription: try-except-finally
# @Author: 子辰
# @Date: 2020-09-08 21:48
# @Software: PyCharm
#################################################
# try-except-finally
#################################################
"""
什么是异常：
    异常即是一个事件，该事件会在程序执行过程中发生，影响了程序的正常执行。
    一般情况下，在python无法正常处理程序时就会发生一个异常。
    异常是python对象，表示一个错误。
    当python脚本发生异常时，我们需要捕捉处理它，否则程序会种植执行
捕获异常的基本方式：
    try:
        语句一：检测语句是否存在错误
    except:
        语句二：若语句一存在错误，可捕获错误
    finally:
        语句三：无论语句一是否存在错误，程序都会执行finally内的代码
常见的异常：
    BaseException           所有异常
    Exception               常规异常错误，，它继承BaseException
    ZeroDivisionError       除0的异常错误
    ValueError              值类型异常错误
"""
def f(num):
    try:
        num / 0
    except ZeroDivisionError as e:
        print(e)
    finally:
        print('执行了finally')
        print('执行结束')

def f1(num):
    try:
        return int(num)
    except ValueError as e:
        print(e)
    finally:
        print('执行结束')

def f2(num):
    try:
        return int(num)
    except (ZeroDivisionError, ValueError) as e:
        print(e)
    finally:
        print('执行结束')
if __name__ == '__main__':
    f2('a')
