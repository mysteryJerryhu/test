# -*- coding:UTF-8 -*-

# 异常处理3
def a(var):
    try:
        return int(var)
    except ValueError, aa:
        print "No number!\n", aa
a("xyz")
