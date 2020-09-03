# 输出格式化
# print(value, ..., sep=',', end='.')
print('lemon', 'lemon', 'lemon', sep=',', end='.');

# 换行  \
print('\n');
print('lemon a apple \
      adegdade');
print("=============================================================")
"""
数学运算
+           加运算
-           减法运算
*           乘法运算
/           除法运算
**          幂运算
%           取余运算
//          取整运算
round()     四舍五入运算

math包中的数学运算:
math.ceil()     向上取整
math.floor()    向下取整
math.trunc()    截取整数位
math.pow()      幂运算函数  eg.math.pow(2,4)  -> 16.0 保留一位小数
"""
print('2 + 3 = ', 2+3)
print('2 - 3 = ', 2-3)
print('2 * 3 = ', 2*3)
print('2 / 3 = ', 2/3)
print('2 ** 3 = ', 2**3)
print('10 % 3 = ', 10%3)
print('5 // 3 = ', 5//3)
import math
print('math.ceil(5.3) = ', math.ceil(5.3))
print('math.floor(5.9) = ', math.floor(5.9))
print('math.trunc(5462.354) = ', math.trunc(5462.354))
print('math.pow(2,3) = ', math.pow(2,3))

print("=============================================================")
"""
字符串链接
1. +  链接符
2. *  多次叠加符
"""
print("lemon" + 'lemon')
print("lemon" * 3)
"""
%s      使用str()函数进行字符串转换
%d      转为十进制整数
%f      转为浮点数  默认保留6位小数  若指定保留小数位数，则 %.nf  n位指定的保留位数
"""
print('lemon %s' %('is girl'))
print("lemon %d" %(21))
print('lemon is %f' %(520))
print('lemon is %.3f' %(520.123456))

"""
字符串格式化
1. %
    print('lemon is %s girl' %('女孩'))
    print('lemon %d years old' %(21))
    print('lemon %f jin' %(21.53))
    print('lemon is %(name)s' %{'name':'lemon'})
    print('lemon %(1)s is lemon, %(0)d years old' %{'21', '柠檬'})
2. format
"""
print('lemon is %s girl' %('女孩'))
print('lemon %d years old' %(21))
print('lemon %f jin' %(21.53))
print('lemon is %(name)s' %{'name':'lemon'})
print('lemon %(name)s is lemon, %(age)d years old' %{'age':21, 'name':'柠檬'})
print('lemon {1} is lemon, {0} years old'.format(21, '柠檬'))
print('lemon {name} is lemon, {age} years old'.format(name='柠檬', age=21))

print("=============================================================")
"""
字符串的切片
"""
# 取第一个字符
print('lemon'[0])
# 取第二个字符
print('lemon'[1])
# 取最后一个字符
print('lemon'[-1])
# 取第2到地4个字符（左闭右开区间） emo
print('lemon'[1:4])
# 取第二个字符以后
print('lemon'[1:])
"""
判断字符串是否以l 开头，以n结尾
"""
print('lemon'.startswith('l'))
print('lemon'.endswith('n'))
"""
获取字符串某个字符的位置
'lemon'.find('e') 找到这个字符，返回下标，多个时返回第一个字符下标，不存在该字符返回-1
'lemon'.index('o')找到这个字符，返回下标，多个时返回第一个字符下标，不存在该字符报错
"""
print('lemon'.find('e'))
print('lemon'.find('k'))
print('lemon'.index('o'))
#print('lemon'.index('k')) -> ValueError: substring not found
"""
字符串替换  'lemon'.replace('m', 'th')
"""
print('lemon'.replace('m','th'))
"""
len('lemon')        返回字符串的长度
'lemon'.upper()     小写转大写
'lemon'.lower()     大写转小写
'lemoon'.count('o') 查找某个字符出现的次数
'lemon'.center(n, '*') 把字符串放中间，两边用 * 补齐，若n小于等于字符串长度，则返回原值
"""
print(len('lemon'))
print('lemon'.upper())
print('LEMON'.lower())
print('lemoon'.count('o'))
print('lemon'.center(9, '*'))

