#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
给定一个字符串代码，然后使用 exec() 来执行字符串代码。
"""
def exec_code():
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC)


if __name__ == '__main__':
    exec_code()
