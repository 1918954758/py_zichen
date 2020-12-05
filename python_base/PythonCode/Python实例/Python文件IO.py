#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 写文件
with open("E:/py/py_zichen/python_base/PythonCode/Python实例/txt/demo.txt", "wt", encoding='utf-8') as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")
# 读文件
with open("E:/py/py_zichen/python_base/PythonCode/Python实例/txt/demo.txt", "rt", encoding="utf-8") as read_file:
    text = read_file.read()

if __name__ == '__main__':
    print(text)
