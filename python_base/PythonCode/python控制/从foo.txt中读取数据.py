#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    # 打开一个文件
    f = open('E:/py/py_zichen/python_base/python基础/python控制/foo.txt', 'r', encoding='utf-8')
    str = f.read()
    print(str)
    # 关闭文件流
    f.close()
