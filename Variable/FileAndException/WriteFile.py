# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: WriteFile
# @Discription: 写入文件
# @Author: 子辰
# @Date: 2020-09-08 20:38
# @Software: PyCharm
############################################
# 写入文件
############################################

"""
open(file, mode = 'w', encoding = 'utf-8', errors = None, newline = None, closefd = True, opener = None)
    file            文件路径
    encoding        编码格式，一般utf-8
    errors          错误级别
    mode            文件打开模式
    newline         区分换行符
    closefd         传入的file参数类型
    mode常用的参数：
        r           只读的方式打开文件
        w           写的方式打开文件
                        如果文件不存在，则新建文件再写入
                        如果文件存在，则覆盖源文件
        a           打开一个文件追加数据
                        如果文件不存在，则新建文件写入
                        如果文件存在，则在末尾处追加内容
"""
'''
1. 写文件
'''
data1 = open('D:\py_zichen\Variable\FileAndException\测试写文件.txt', mode = 'w', encoding = 'utf-8')
data1.write('\nhello lemon')
data1.close()
'''
2. 写文件
'''
with open('D:\py_zichen\Variable\FileAndException\测试写文件1.txt', mode = 'w', encoding = 'utf-8') as data2:
    data2.write('又写入了一个lemon\n又写入了一个lemon')
'''
3. 写文件
'''
with open('D:\py_zichen\Variable\FileAndException\测试写文件1.txt', mode = 'w', encoding = 'utf-8') as data3:
    data3.writelines('lemonlemonlemonlemonlemonlemonlemon\nlemonlemonlemone')
'''
4. 写文件，传入序列
'''
with open('D:\py_zichen\Variable\FileAndException\测试写文件1.txt', mode = 'a', encoding = 'iso8859-1') as data4:
    data4.writelines(['lemon\n', 'lemon\n', 'lemon\n', 'lemon\n', 'lemon\n'])

