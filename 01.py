# -*- coding: utf-8 -*-
# 使用中文注释时，开头必须加上如上语句
a = 1       # a 类整型, 0开头八进制数, 0x开头16进制数
a1 = -2
a2 = 0x69
a3 = -0x26
a4 = 010
b = 45164646L     # b 类长整型, 后面带 'L'
b1 = -0x112L
b2 = -15646L
b3 = 0xDEFL
c = 0.2           # c 类浮点型
c1 = -21.9
c2 = 32.3e+18
c3 = -32e100
d = 3.14j            # d 类复数, 可支持 a + bi, 也可以使用 complex(a, b), 实部a, 虚部b
d1 = -9.3-36j
d2 = 9+6j

print a, a1, a2, a3, a4, b, b1, b2, b3, c, c1, c2, c3, d, d1, d2

m = 10
n = 22

v1 = m + n
v2 = n - m
v3 = m * n
v4 = m / n     # 以上为基础加减乘除(整数除以整数得到整数，需要小数需要浮点数)
v5 = m ** n    # 2次方
v6 = n % m     # 取余数
v7 = n // m    # 取整数
print v1, v2, v3, v4, v5, v6, v7

# Python 还支持比较运算符（大于，小于，等于，不等于，大于等于，小于等于）
# a += b 就是 a = a + b, 其他运算类似

tuple = ('runoob', 786, 2.23, 'john', 70.2)  # Python 元组, 若为 [] 则为列表, 只有列表可重新赋值
tinyuple = (123, 'john')           # {key:value} 为字典, 由索引key和对应的值value构成, ：来区别

print tuple
print tuple[0]
print tuple[1:3]   # 输出头部序号和到尾部序号内, 尾部序号不输出
print tuple[2:]   # 从第3个开始一直到最后，[：]代表全部输出
print tinyuple * 2  # 输出两次
print tuple + tinyuple  # + 代表连接
