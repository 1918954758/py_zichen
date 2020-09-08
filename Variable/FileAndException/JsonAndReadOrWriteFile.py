# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: JsonAndReadOrWriteFile
# @Discription: Json与文件的读写
# @Author: 子辰
# @Date: 2020-09-08 21:03
# @Software: PyCharm
##############################################
# Json与文件的读写
##############################################
"""
Json(javaScript Object Notation)特点：
    1. Json 是一种轻量级数据交换格式，易于阅读和编写
    2. Json 是具有通用性，支持几乎所有的语言
    3. Json 支持跨平台，支持windows, linux，Mac平台
Json 常用函数
    json.dumps()        将Python对象编写成json字符串
    json.loads()        将已编码的json字符串解码为Python对象
    json.dump()         将json字符串数据写进文件
    json.load()         读取json文件里面的数据

    python              {'lemon1':1, 'lemon2':2, 'lemon':3}
                        {"lemon1":1, "lemon2":2, "lemon":3}
    json                '{"lemon1":1, "lemon2":2, "lemon":3}'
json 与 pyton 类型转换
    json                    pyton
    object                  dict
    array                   list,tuple
    string                  str
    number                  int,float
    true                    True
    false                   False
    null                    None
"""

import json


def f1():
    ''' 对python对象进行操作 '''
    # json.dumps()
    # 将python对象转成json字符串
    # json.loads()
    # 将json字符串转成python
    p_list = [
        {'lemon': True, 'apple': 6},
        {'pear': 6, 'banana': False}
    ]
    p_dict = {'python': 1, 'java': 2, 'Hadoop': 3}
    json_list = json.dumps(p_list)
    json_dict = json.dumps(p_dict)

    python_list = json.loads(json_list)
    python_dict = json.loads(json_dict)


def f2():
    ''' 文件读写 '''
    # json.dump()  写 将json字符串数据写进文件
    # json.load()  度 读取json文件里面的数据

    # 写入json文件
    p_dict = '{"python" : 1, "java" : 2, "Hadoop" : null, "lemon" : true, "banana" : false}'
    with open('D:\py_zichen\Variable\FileAndException\测试写json文件1.txt', mode = 'w', encoding = 'utf-8') as f:
        json.dump(p_dict, f)

    # 读取json文件
    with open('D:\py_zichen\Variable\FileAndException\测试写json文件1.txt', mode = 'r', encoding= 'utf-8') as f1:
        data = json.load(f1)
        print(data)
        data1 = json.loads(data)
        print(data1)
if __name__ == '__main__':
    f2()