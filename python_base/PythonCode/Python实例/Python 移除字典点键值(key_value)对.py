#!/usr/bin/python
# -*- coding: UTF-8 -*-
test_dict = {"Runoob": 1, "Google": 2, "Taobao": 3, "Zhihu": 4}

if __name__ == '__main__':
    print(test_dict)
    # 使用 del
    del test_dict["Runoob"]
    print(test_dict)
    # 使用pop
    print('====================')
    print(test_dict)
    test_dict.pop("Google")
    print(test_dict)
    # 使用 items  字典推导式
    print('====================')
    print(test_dict)
    print({k: v for k, v in test_dict.items() if k != 'Taobao'})
    # 类似列表推导式 [i for i in "adfsdaf" if i != 'd']
