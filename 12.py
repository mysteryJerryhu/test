# -*- coding:UTF-8 -*-
# 使用中文注释时，开头必须加上如上语句

def date():
    import calendar
    import time
    a = input("Enter year(after 1970)：")
    b = input("Enter month：")
    cal1 = calendar.month(a, b)
    print cal1, "Localtime：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return
date()


