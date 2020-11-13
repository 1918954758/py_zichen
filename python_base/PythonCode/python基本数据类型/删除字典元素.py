#!/usr/bin/python
# -*- coding: UTF-8 -*-

dict = {'Name': 'Runoob', 'Age': 21, 'Class': 'First'}

if __name__ == '__main__':
    print('dict：', dict)
    del dict['Name']  # 删除字典中Name元素
    print('dict：', dict)
    dict.clear()  # 清空字典
    print('dict：', dict)
    del dict  # 删除字典dict
    print("dict['Age']：", dict['Age'])
    print("dict['School']：", dict['School'])
