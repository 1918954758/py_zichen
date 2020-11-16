#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('名称：%s' % self.name)


stu = Student('xiaoming')
if __name__ == '__main__':
    stu()
