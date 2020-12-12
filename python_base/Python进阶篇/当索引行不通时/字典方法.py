#!/usr/bin/python
# -*- coding:UTF-8 -*-
from copy import deepcopy

if __name__ == '__main__':
    d = {}
    """clear"""
    print("\"\"\"clear()\"\"\"")
    d['key'] = 'value'
    print(d)
    d.clear()
    print(d)
    print('==================')
    # eg 1
    x = {}
    y = x
    x['key'] = 'value'
    print(x)
    x = {}
    print("x是{}; y是{}".format(x, y))
    # eg 2
    i = {}
    j = i
    i['key'] = 'value'
    i.clear()
    print("i是{}; j是{}".format(i, j))
    """copy"""
    print("\"\"\"copy()\"\"\"")
    # 浅复制 copy()  复制值，但是内存地址不会发生改变，所以当原字典改变，复制后的字典也会改变
    c1 = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
    c2 = c1.copy()
    print(c1)
    print(c2)
    print(c2['machines'])
    # 深复制 deepcopy()  复制内存地址，所以当原字典改变，复制后的字典是不会改变的
    # from copy import deepcopy
    c3 = {}
    c3['names'] = ['Alfred', 'Bertrand']
    c4 = c3.copy()
    print("c4:{}".format(c4))
    dc3 = deepcopy(c3)
    print("dc3:{}".format(dc3))
    c3['names'].append('Clive')
    print("c4:{}".format(c4))
    print("dc3:{}".format(dc3))
    """fromkeys()"""
    print("\"\"\"fromkeys()\"\"\"")
    a = {}.fromkeys(['name', 'age'])  # 创建键，值为None
    print("a:{}".format(a))
    b = dict.fromkeys(['name', 'age'])
    print("b:{}".format(b))
    c = dict.fromkeys(['name', 'age'], ('zichen', 28))  # 复制同一的默认值
    print("c:{}".format(c))
    e = dict.fromkeys({'name': 'zichen', 'age': 28})  # 虽然给了值，但是只有key起作用
    print("e:{}".format(e))
    """get()"""
    print("\"\"\"get()\"\"\"")
    f = {}
    # print(f['name']) 访问没有的key会报错
    print(f.get('name'))  # 访问没有的key不会报错，返回None
    """items"""
    # 返回包含字典的项的列表
    print("\"\"\"items()\"\"\"")
    g = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
    it = g.items()
    print("items:{}".format(it))
    # output => items:dict_items([('username', 'admin'), ('machines', ['foo', 'bar', 'baz'])]) 字典视图
    print("转成list:{}".format(list(it)))
    """keys"""
    print("\"\"\"keys()\"\"\"")
    print("keys:{}".format(g.keys()))
    """values"""
    print("\"\"\"values()\"\"\"")
    print("values:{}".format(g.values()))
    """pop"""
    # list.pop() 删除字典最后一个键值对
    print("\"\"\"pop()\"\"\"")
    # 获取指定键的值，并将该键值从字典中移除
    h = {'username': 'admin', 'password': '123456', 'email': 'www.ziChen.com'}
    t = h.pop("password")
    print("t:{}".format(t))
    print("h:{}".format(h))
    """popitem"""
    print("\"\"\"popitem()\"\"\"")
    # list.popitem() 随机删除字典中的键值对，因为字典的键值对是无序的，故此也就没有最后一个的概念
    l = {1: 2, 3: 4, 5: 6, 7: 8, 9: 10, 2: 1, 4: 3, 6: 5, 11: 12, 13: 14}
    print("l:{}".format(l))
    print("l.popitem:{}".format(l.popitem()))
    print("l.popitem:{}".format(l.popitem()))
    print("l.popitem:{}".format(l.popitem()))
    print("l.popitem:{}".format(l.popitem()))
    print("l.popitem:{}".format(l.popitem()))
    """setdefault"""
    print("\"\"\"setdefault()\"\"\"")
    m = {}
    print(m.setdefault('name', 'N/A'))  # 返回的结果形式get()
    print(m)
    m.setdefault('name', 'A/N')
    print(m)
    m['name'] = 'GumBy'
    print(m)
    print(m.setdefault('name', 'N/A'))
    """update"""
    # 使用一个字典来更新另一个字典
    n = {'a': 12, 'b': 23}
    o = {'name': 'A/N', 'age': 23}
    print("n:{}".format(n))
    print("o:{}".format(o))
    print("update after")
    n.update(o)
    print("n:{}".format(n))
    print("o:{}".format(o))
