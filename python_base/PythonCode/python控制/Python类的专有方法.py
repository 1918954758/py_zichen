#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return '学生名称： %s' % self.name


if __name__ == '__main__':
    print(Student('小明'))
