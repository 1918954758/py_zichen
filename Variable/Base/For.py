# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: For
# @Discription: for 循环
# @Author: 子辰
# @Date: 2020-09-05 13:31
# @Software: PyCharm

"""
for 循环遍历一个可迭代对象，主要用来遍历序列（list, str, dict)、字典和集合
for 循环变量 in 可迭代对象:
    <语句1>
else:
    <语句2>
else可以与for循环搭配使用，当for循环执行结束后，会执行else语句中的内容
"""

word = "I am lemon"
for i in word:
    print(i, end="")
else:
    print("\nfor循环之后的其他逻辑操作")
print("遍历字符串结束")
print("》》》》》》》》》》》》》》》》》《《《《《《《《《《《《《《《《《《《")

fruits_list = ['banana', 'mango', 'lemon']
for i in fruits_list:
    print(i, end=' ')
print("遍历列表结束")
print("》》》》》》》》》》》》》》》》》《《《《《《《《《《《《《《《《《《《")

fruits_dict = {'banana': 5, 'mango': 1, 'lemon': 7}
for i in fruits_dict.keys():
    print(i, end=" ")
print("遍历字典的key结束")
for i in fruits_dict.values():
    print(i, end=" ")
print("遍历字典的值结束")
for key, value in fruits_dict.items():
    print(key, value, end=" ")
print("遍历字典的键和值结束")
for i in fruits_dict.items():
    print(i, end=" ")
print("把字典的键值对拿出来，分别作为一个set集合")
print("》》》》》》》》》》》》》》》》》《《《《《《《《《《《《《《《《《《《")

complex_list = [['banana', 'mango', 'lemon'], [1, 2, 3]]
for i in complex_list:
    print("列表的内容：", i, end = " ")
    for x in i:
        print("子列表内容：", x, end = " ")
