#!/usr/bin/python
# -*- coding:UTF-8 -*-
if __name__ == '__main__':
    setter = set()
    with open("E:\\py\\py_zichen\\python_base\\PythonCode\\file\\txt\\orgin.txt", 'r', encoding="UTF-8") as readFile:
        fileContext = readFile.readlines()
        print("处理后的集合为：{}，集合长度为：{}".format(fileContext, len(fileContext)))
        for i in range(0, len(fileContext)):
            setter.add(fileContext[i])
        print("处理后的集合为：{}，集合长度为：{}".format(setter, len(setter)))
    with open("E:\\py\\py_zichen\\python_base\\PythonCode\\file\\txt\\write2.txt", 'w', encoding="utf-8") as writeFile:
        for i in range(0, len(setter)):
            writeFile.write(list(setter)[i])
