# -*- coding:UTF-8 -*-
# 使用中文注释时，开头必须加上如上语句

# 基本时间日历的输出

import time          # 导入时间模块
import calendar      # 导入日历模块

ticks = time.time()          # time.time()输出时间
print "Time segment:", ticks       # 时间段，从1970年1月1日开始计算秒数

localtime = time.localtime()
print "Localtime:", localtime       # 元组时间输出

localtime2 = time.asctime(time.localtime())
print "Localtime:", localtime2        # 默认格式化时间 time.asctime()

print "Localtime:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 按需求格式化时间 time.strftime()
# %Y:四位数年份 %m:月份 %d:月内某一天 %H:24小时制 %M:分钟 %S:秒  其他具体查询

cal = calendar.month(2017, 8)     # 输出2017年8月的日历  calendar.month()
print cal
cal1 = calendar.month(input("Enter year:"), input("Enter month:"))   # 手工输入年份月份输出
print cal1
'''
其他时间和日历的模块和函数，具体自行查询
'''
