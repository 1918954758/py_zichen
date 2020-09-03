# @discription: 列表，元组和字典
"""
列表：可以把大量的数据房子一起进行集中处理的。列表时方括号'[]'包围的数据集合，不同成员以 ','分割.列表中可以包含任何数据类型，列表通过下标索引访问其中成员
    列表是有序的序列，每个元素都分配一个下标索引。第一个是0，第二个是1，以此类推
"""
# 列表的创建 list() 或[]
list()
[]
print(list())
print([])
# 创建有元素的列表
numbers = [1, 2, 3, 4, [7, 8, 9, 6, 0]]
print(numbers)
print(numbers[0])
print(numbers[4][2])

# 列表之间的相加  不支持相减，相乘，相除
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 + list2)
# 列表可以用重复符来操作
print(list1 * 3)
"""
列表的基本操作
list.count(x)           统计列表中x 出现的次数，若不存在，则返回0
list.append(x)          向列表尾部增加新成员  如果x也是一个列表，那么会把这个列表当成元素添加到末尾
list.extend(list2)      向列表尾部追加另外一个列表（添加的是另一个列表的值）
list.index(x)           返回参数x在列表中的序号，若不存在，则报错
list.insert(index, object)  向列表指定部位增加新成员
list.pop()              默认删除列表尾部成员，并返回删除的成员 （如果指定需要，则删除指定序号的成员）
list.remove(x)         删除列表中指定的成员（有多个的话，只删除第一个），若指定的成员不存在，则报错
list.reverse()          将列表成员顺序颠倒
list.sort()             将列表成员进行排序（要求成员间可以排序，否则报错）  （可以指定倒叙  list.sort(reverse=True)）
"""
arr1 = [2, 5, 7, 8, 9, 5, 7, 0, 9, 1, 6]
arr2 = [4, 5, 6, 4, 3]
print(arr1.count(9))
arr1.append(10)
print(arr1)
arr1.extend(arr2)
print(arr1)
print(arr1.index(4))
arr2.insert(0, 1)
print(arr2)
arr2.pop()
print(arr2)
arr2.remove(6)
print(arr2)
arr2.reverse()
print(arr2)
print(arr1)
arr1.sort()
print(arr1)
arr1.reverse()
print(arr1)
arr3 = [2, 3, 5, 1, 3, 65, 3, 7, 8, 454, 5, 4, 26, 57, 9, 5, 86]
print(arr3)
arr3.sort()
print(arr3)
arr3.sort(reverse=True)
print(arr3)

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
