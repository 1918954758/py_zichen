# -*- coding utf-8 -*-
# @ProjectName: py_zichen
# @Script: GuessNumberGame
# @Discription: 猜数字游戏，学习玩python基本数据类型，list，tuple,dict,set,for,while 之后的小练习
# @Author: 子辰
# @Date: 2020-09-05 19:53
# @Software: PyCharm

"""
随机整数 0 - 9
用户输入数字，如果输入的数字不等于答案，则出现比答案大，还是比答案小的提示；若等于答案，游戏结束，显示答案。
游戏只能才三次，若三次猜中，游戏闯关成功，并显示答案
若游戏三次内未猜中，游戏闯关失败，并显示答案
"""
import random
random_num = random.randint(0, 9)
times = 3
while times > 0:
    ''' 用户输入一个数，进行比较 '''
    guess_num = int(input('请输入 0 - 9 整数 '))
    if guess_num > random_num:
        print('大了')
    elif guess_num < random_num:
        print('小了')
    else:
        print('猜中了，正确答案是：' + str(random_num))
        break
    times -= 1
    if times == 0:
        print('您三次都未猜中，正确答案是： ' + str(random_num))





# inpt = int(3)
# rang = range(1, 7)
# count = 1
# while count <= 3:
#     if inpt < rang:
#         print('小了')
#         count += 1
#     elif inpt > rang:
#         print('大了')
#         count += 1
#     else:
#         print('游戏结束！', rang)
#         break