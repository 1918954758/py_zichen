#!/usr/bin/python
# -*- coding: UTF-8 -*-
sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
print(sites)  # 输出集合，重复的元素被自动去掉
# 成员测试
if 'Runoob' in sites:
    print('Runoob在集合中')
else:
    print('Runoob不在集合中')
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
if __name__ == '__main__' :
        print(a)
        print(a - b)  # a 和 b的差集
        print(a | b)  # a 和 b的并集
        print(a & b)  # a 和 b的交集
        print(a ^ b)  # a 和 b中不同时存在的元素
