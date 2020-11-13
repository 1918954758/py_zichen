#!/usr/bin/python
# -*- coding: UTF-8 -*-

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

if __name__ == '__main__':
    lis1 = [[row[i] for row in matrix] for i in range(4)]
    print(lis1)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
if __name__ == '__main__':
    print(transposed)

tr = []
for i in range(4):
    tr_row = []
    for row in matrix:
        tr_row.append(row[i])
    tr.append(tr_row)

if __name__ == '__main__':
    print(tr)