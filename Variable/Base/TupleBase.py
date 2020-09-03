# @ProjectName: py_zichen
# @Script: TupleBase
# @discription: 列表，元组和字典
# @Author: 子辰
# @Date: 2020-09-04 00:44

"""
元组（tuple）：元组是圆括号()包围的数据集合，可以通过序号访问元素
            元组可以理解为特殊的列表
            元组的元素一旦创建，是不可以改变的
            虽然元组的元素是不可变的，但是，如果元组的元素是列表或者字典时，列表或字典的内容是可以改变的
"""
# 创建元组
()
tuple()
print(())
print(tuple())
# 创建一个元素的元组
t1 = (1,)
t2 = (1)
print(type(t1))  # <class 'tuple'>
print(type(t2))  # <class 'int'>
'''可见创建一个元素的元组，逗号是不能省略的'''
tuple1 = (1, 2, 3)
print(tuple1)
print(type(tuple1))
# 访问元组
a = tuple1[0]
print(a)
# 修改元组元素会报错  切记
tuple2 = (1, 2, 3, 3, [2, 3, 4, 6])
b = tuple2[4][3] = 10
print(b)
print(tuple2)
"""
元组常见函数
len(tuple)      返回元组数量
max(tuple)      返回元组最大值
min(tuple)      返回元组最小值
tuple(seq)      将序列转为元组
"""
tuple3 = (1, 2, 3, 5, 6, 4, 6, 3, 5, 25, 26, 425, 6, 4)
print(len(tuple3))
print(max(tuple3))
print(min(tuple3))

array = [3, 4, 5, 6, 5, 76, 8, 79, 3, 7, 8456, 64, 23]
print(array)
print(type(array))
tuple4 = tuple(array)
print(tuple4)
print(type(tuple4))
print(type(array))
