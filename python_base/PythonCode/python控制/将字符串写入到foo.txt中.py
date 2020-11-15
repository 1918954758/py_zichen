#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    # 打开一个文件
    f = open("E:/py/py_zichen/python_base/python基础/python控制/foo.txt", "w", encoding='utf=8')
    f.write("Python 是一个非常好用的语言。\n是的，的确非常好用！！\n",)
    # 关闭打开的文件
    f.close()
