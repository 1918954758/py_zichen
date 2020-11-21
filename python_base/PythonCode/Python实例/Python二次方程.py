#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 二次方程式 ax ** 2 + bx + c = 0
# a b c 用户提供，为实数，a ≠ 0
# 导入 cmath(复杂数学运算)模块
import cmath

a = float(input("请输入 a: "))
b = float(input("请输入 b: "))
c = float(input("请输入 c: "))

# 计算 Δ
Δ = (b ** 2) - 4 * a * c

if __name__ == '__main__':
    # 求解
    # sol1 = (-b + cmath.sqrt(Δ)) / (2 * a)
    # sol2 = (-b - cmath.sqrt(Δ)) / (2 * a)
    # print('结果为 {0} 和 {1} '.format(sol1, sol2))
    if a == 0 and b == 0 and c == 0:
        print("有无穷多个解")
    elif Δ > 0:
        sol1 = (-b - cmath.sqrt(Δ)) / (2 * a)
        sol2 = (-b + cmath.sqrt(Δ)) / (2 * a)
        print('结果为 {0} 和 {1} '.format(sol1, sol2))
        print('结果为 {0:.3f} 和 {1:.3f} '.format(sol1, sol2))
    else:
        print("无解")
