# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: SetConnection
# @Discription:  set 集合
# @Author: 子辰
# @Date: 2020-09-05 00:53
# @Software: PyCharm

# 创建集合
s1 = set()
print(s1, type(s1))

# 创建含有多个元素的集合
a = {1, 2, 3, 4, 5}
print(a, type(a))
"""
集合不支持索引查找元素
a[0]  会报错
"""
# 集合特点：唯一性
# 如果创建一个集合，集合里的内容有重复的元素，set()会去重，这点和Java中的set一样会去重
b = {1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 77, 7, 7, 77.8, 8}
print(b, type(b))

# 如果想对一个列表进行去重的话，那么可以利用set来操作
c = ['lemon', 'lemon', 'apple', 'apple', 'apple', 'banana', 'banana']
print(set(c))

# 获取集合的元素个数
d = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 2, 4, 1, 8}
e = {1, 3, 6, 8, 9}
print(type(len(d)), type((len(e))))
print('d集合的元素个数是: %d' % (len(d)), '\n e集合的元素个数是: %d' % (len(e)))

# 判断某个元素是否在结合d 中
print('a' in d)
print(1 in d)

# 求两个集合的差集  减数中的数不会增加，只是判断减数中有没有被减数中的元素，有则舍去，无则忽略
print('集合e和集合d的差集：', e - d)
print('集合d和集合e的差集：', d - e)
# 求两个集合的交集
print('集合d和集合e的交集：', d & e)
# 求两个集合的并集
print('集合d和集合e的并集：', d | e)
# 求两个集合的对称差   就是取两个集合不重复的部分
print('集合d和集合e的对称差：', d ^ e)