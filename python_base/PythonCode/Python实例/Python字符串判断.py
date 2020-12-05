#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    # 测试实例一
    print("测试实例一")
    str1 = "runoob.com"
    print(str1.isalnum())  # 判断所有字符都是数字或者字母
    print(str1.isalpha())  # 判断所有字符都是字母
    print(str1.isdigit())  # 判断所有字符都是数字
    print(str1.islower())  # 判断所有字符都是小写
    print(str1.isupper())  # 判断所有字符都是大写
    print(str1.istitle())  # 判断所有单词都是首字母大写，像标题
    print(str1.isspace())  # 判断所有字符都是空白字符、\t、\n、\r

    print("------------------------")

    # 测试实例二
    print("测试实例二")
    str2 = "runoob"
    print(str1.isalnum())
    print(str1.isalpha())
    print(str1.isdigit())
    print(str1.islower())
    print(str1.isupper())
    print(str1.istitle())
    print(str1.isspace())
