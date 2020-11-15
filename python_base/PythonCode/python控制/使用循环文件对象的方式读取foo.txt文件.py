#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    # 打开一个文件
    f = open("E:/py/py_zichen/python_base/python基础/python控制/foo.txt", 'r', encoding='utf-8')
    for line in f:
        print(line)
    # 关闭打开的文件
    f.close()
