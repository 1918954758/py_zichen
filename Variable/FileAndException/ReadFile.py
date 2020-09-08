# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: ReadFile
# @Discription: 读取文件
# @Author: 子辰
# @Date: 2020-09-08 20:06
# @Software: PyCharm

############################################
# 读取文件
############################################
"""
1. Python open 函数
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, open=None)
    参数说明：
        file                文件路径(相对路径或者绝对路径)
        mode                可选，文件打开方式
        encoding            编码格式，一般utf-8

        buffering           设置缓冲
        errors              报错级别
        newline             区分换行符
        closefd             传入的file参数的类型
        mode：常用参数说明：
            r           只读的方式打开文件
            w           写的方式打开文件
                            如果该文件不存在，创建新文件
                            如果该文件存在，则覆盖源文件
            a           打开一个文件用于追加
                            如果该文件不存在，创建新文件进行写入
                            如果该文件存在，则在原有文件结尾追加写入

"""
'''
1. 读取文件方式，得手动关闭文件
'''
'''
f = open('D:\py_zichen\Variable\FileAndException\ReadFile.py', mode = 'r', encoding = 'utf-8')
data = f.read()
print(data)
f.close()
'''
'''
2. 使用 with open()的方式，该方法不需要手动关闭文件
'''

with open('D:\py_zichen\Variable\FileAndException\ReadFile.py', mode = 'r', encoding = 'utf-8') as f1:
    data2 = f1.read();
    print(data2)

'''
3.文件读取的格式：
    with open(file, mode = 'r', encoding = 'utf-8') as f:
        f.read()                返回整个文件数据，如果大文件，不介意使用这种方式
        f.readline()            返回第一行数据
        f.readlines()           以列表的形式逐一返回文件数据，每一行都是列表的一个元素
'''
with open('D:\py_zichen\Variable\FileAndException\测试文本.txt', mode = 'r', encoding = 'utf-8') as f2:
    data3 = f2.readline()
    print(data3)