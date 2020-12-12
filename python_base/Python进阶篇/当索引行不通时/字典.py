#!/usr/bin/python
# -*- coding:UTF-8 -*-

if __name__ == '__main__':
    # 每一个键值对，称之为项(item)
    phoneBook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

    # 使用dict创建字典
    items = {('name', 'Gumby'), ('age', 42)}
    d = dict(items)
    print(d)
    # output =>{'name': 'Gumby', 'age': 42}

    print(d['name'])  # output => Gumby

    # 使用关键字实参调用字典
    di = dict(name='GumBy', age=42)
    print(di)

    # 字典的基本操作
    '''1. len(d)'''
    print(len(d))
    '''2. d[k]'''
    print(d['age'])
    '''3. d[k] = v'''
    d['age'] = 25
    d['sex'] = '女'
    print(d)
    '''4. del d[k]'''
    del d['sex']
    print(d)
    '''5. k in d'''
    if 'class' in d:
        print('d中有class键')
    else:
        print('d中无class键')
    if 'age' in d:
        print('d中有age键')
    else:
        print('d中无age键')

    # 给字典赋值
    nullDict = {}
    nullDict.update({'name': 'zichen'})
    nullDict['age'] = 28
    print(nullDict)

    print('====================')

if __name__ == '__main__':
    # 电话号码的使用
    people = {
        'Alice': {
            'phone': '2341',
            'addr': 'Foo drive 23'
        },
        'Beth': {
            'phone': '9102',
            'addr': 'Bar street 42'
        },
        'Cecil': {
            'phone': '3158',
            'addr': 'Baz avenue 90'
        }
    }
    # 电话号码和地址的描述性标签，供打印输出时使用
    labels = {
        'phone': 'phone number',
        'addr': 'address'
    }
    name = input('Name:')
    # 要查找正确的电话号码地址？
    request = input('Phone number (p) or address (a)?')
    # 使用正确的键
    if request == 'p':
        key = 'phone'
    if request == 'a':
        key = 'addr'
    # 仅当名字是字典包含的键时才打印信息：
    if name in people:
        print(" {}'s {} is {}.".format(name, labels[key], people[name][key]))
    else:
        print(" {}'s not in people".format(name))
    print('====================')

# 将字符串格式设置功能用于字典
if __name__ == '__main__':
    temple = '''<html>
<head>
    <title value='{title}'/>
    <meta encoding='utf-8'/>
</head>
<body>
    <h1>{title}</h1>
    <p>{text}</p>
</body>'''
    data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
    print(temple.format_map(data))
