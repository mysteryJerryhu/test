# -*- coding: utf-8 -*-
# 使用中文注释时，开头必须加上如上语句
a = 10
b = 20
c = 0
list = [1, 2, 3, 4, 5]

c = a & b
print "c is ", c     # 按位 与 运算, 11运算得1, 否则为0

c = a | b
print "c is ", c     # 按位 或 运算, 两者只要一个为1, 即为1

c = a ^ b
print "c is ", c     # 按位 异或 运算, 两者不同, 为1

c = ~ a
print "c is ", c     # 按位 取反 运算, 1变0, 0变1

c = a << 2
print "c is ", c      # 移位运算, 左移

c = a >> 2
print "c is ", c       # 移位运算, 右移

if a in list:
    print "variable a in the list"
else:
    print "variable a not in the list"      # in 运算, 在序列中有指定值, 返回true, 否则false

if b not in list:
    print "variable b not in the list"
else:
    print "variable b in the list"          # not in 运算, 和 in 情况相反

if a is b:
    print "a and b have same tag"
else:
    print "a and b not same"       # is 运算, 判断两个对象(非值)是否相同, 相同true, 否则false

if a is not b:
    print "a and b not same"
else:
    print "a and b have same tag"      # is not 运算, 和 is 运算情况相反
