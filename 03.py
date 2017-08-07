# -*- coding: utf-8 -*-
# 使用中文注释时，开头必须加上如上语句
a = 0
b = 1
if (a > 0) and (b / a > 2):
    print "yes"
else:
    print "no"            # and 运算, 返回最后一个非0值, 报“忧”
# not and 运算即为 非 运算, true 返回 false, false 返回 true

if (a > 0) or (b / a > 2):
    print "yes"
else:
    print "no"            # or 运算, 返回第一个非0值, 报“喜”
# 没有（）下, and 优先 or
