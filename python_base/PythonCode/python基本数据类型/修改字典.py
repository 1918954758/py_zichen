#!/usr/bin/python
# -*- coding: UTF-8 -*-

dicts = {'Name': 'Runoob', 'Age': 21, 'Class': 'First'}

if __name__ == '__main__':
    print("dicts：", dicts)
    dicts['Age'] = 8  # 更新Age
    dicts['School'] = "菜鸟教程"  # 添加信息
    print("dicts['Age']：", dicts['Age'])
    print("dicts['School']：", dicts['School'])
    print("dicts：", dicts)
