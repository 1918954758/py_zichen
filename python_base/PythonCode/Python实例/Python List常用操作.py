#!/usr/bin/python
# -*- coding: UTF-8 -*-
li1 = ['1', 'a', 'r', '5', 4, 'yo', 'lemon', 'we', 'fight']

# List索引        list[1:5]   list[-5:-2]
if __name__ == '__main__':
    print(li1[2:4])  # ['r', '5']
    print(li1[-5:-2])  # [4, 'yo', 'lemon']
    print(li1[-1])  # fight
    print(li1[-9])  # 1

print('================')
li2 = ['2', 3, 'a', 5]
# 增加元素      list.append('d')    list.insert(2, 'a')     list.extend(['a', 'b', 'c'])
if __name__ == '__main__':
    print(li2)

    li2.insert(1, 'new')  # 想某个位置添加元素
    print(li2)

    li2.append('l')  # 只能增加一个元素
    # li2.append('e', 't')
    print(li2)

    li2.extend(['i', 'o', 'u'])  # 增加一个列表
    print(li2)

print('================')
# list搜索 即 查找元素对应的索引   list.index('x')
li3 = ['2', 3, 'a', 5]
if __name__ == '__main__':
    print(li3.index(3))
    print(li3.index('a'))

print('================')
# list删除元素  del list        list.remove('x')    list.pop()
li4 = ['2', 3, 'a', 5, 't', 'u', 'p']
if __name__ == '__main__':
    print(li4)
    del li4[2]
    print(li4)
    li4.remove('t')
    print(li4)
    li4.pop()
    print(li4)

print('================')
# list 运算符  * +=
li5 = [1, 2, 3, 4]
if __name__ == '__main__':
    print(li5 * 3)
    print(li5 + ['a', 'b'])
    li5 += ['c']
    print(li5)

print('================')
# 使用join链接list成为字符串  ';'.join('%s=%s'.format(k, v) for k, v in s.items())
li6 = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
if __name__ == '__main__':
    print(['%s=%s' % (k, v) for k, v in li6.items()])
    print(';'.join(['%s=%s' % (k, v) for k, v in li6.items()]))
    print('  '.join(['%s=%s'.format(k, v) for k, v in li6.items()]))

print('================')
# list 分割字符串  s.split
li7 = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
if __name__ == '__main__':
    s = ';'.join(li7)
    print(s)
    print(s.split(";"))
    print(s.split(';', 1))

print('================')
# list 的映射解析  [i for i in list]
li8 = [2, 3, 6, 4, 7, 8, 9]
if __name__ == '__main__':
    print([i * 2 for i in li8])
    print([i // 2 for i in li8])

print('================')
# dictionary 中的解析 dict.keys()  dict.values()  dict.items()  ['%s=%s' % (k, v) for k, v in dict.items()]
li9 = {"server": "mpilgrim", "database": "master", "uid": "sa", "pwd": "secret"}
if __name__ == '__main__':
    print(li9)
    keysLi9 = li9.keys()
    print(keysLi9)
    valuesLi9 = li9.values()
    print(valuesLi9)
    itemsLi9 = li9.items()
    print(itemsLi9)
    print()
    print([k for k, v in li9.items()])
    print([v for k, v in li9.items()])
    print(['%s=%s' % (k, v) for k, v in li9.items()])
    print(['%s = %s'.format(k, v) for k, v in li9.items()])  # 解析不了 '%s=%s'.format(k, v)

print('================')
# list 过滤  [i for i in list if len(i) != '3']
li10 = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
if __name__ == '__main__':
    print(li10)
    print([i for i in li10 if len(i) > 1])
    print([i for i in li10 if i != 'b'])
    print([i for i in li10 if len(i) == 1])
