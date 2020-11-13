#!/usr/bin/python
# -*- coding: UTF-8 -*-

knights = {'a': 1, 'b': 2, 'c': 3}
if __name__ == '__main__':
    for k, v in knights.items():
        print(k, v)
print('=============================')
lst = [1, 2, 3, 4, 5, 6, 7, 8]
if __name__ == '__main__':
    for i, v in enumerate(lst):
        print(i, v)
print('=============================')
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]
if __name__ == '__main__':
    for ls1, ls2 in zip(lst1, lst2):
        print(ls1, ls2)
print('=============================')
lst3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
if __name__ == '__main__':
    for ls3 in reversed(lst3):
        print(ls3)
print('=============================')
lst4 = [4, 3, 7, 3, 9, 2, 1, 5, 3, 6]
if __name__ == '__main__':
    for i in sorted(lst4):
        print(i)
    print('----------')
    for ls4 in sorted(set(lst4)):
        print(ls4)