#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student(object):

    def __init__(self, name):
        self.name = 'xiaoming'

    def __getattr__(self, attr):            # 可以增加类的属性，此外看还可以直接添加类属性
        if attr == 'score':
            return 96


stu = Student('xiaoming')
if __name__ == '__main__':
    print(stu.name)
    print(stu.score)
