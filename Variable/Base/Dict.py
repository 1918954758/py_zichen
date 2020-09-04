# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: Dict
# @Discription: 字典基础知识
# @Author: 子辰
# @Date: 2020-09-05 00:38
# @Software: PyCharm

# 创建字典  dict
dict1 = {}
dict2 = dict()
print(dict1, dict2)

# 从字典中获取数据
dict3 = {"lemon":"柠檬", "age":21, "hobby":"money"}
name = dict3["lemon"]
age = dict3["age"]
hobby = dict3["hobby"]
print(name, age, hobby)

# 增加新成员
print(dict3)
dict3["sex"] = "女"
print(dict3)

# 删除字典成员
del dict3["age"]
print(dict3)  # 删除指定成员
dict3.clear()   # 清空字典dict3
print(dict3)
#del dict3   删除字典dict3
