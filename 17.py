# -*- coding:UTF-8 -*-

# 异常处理3
# 观察如下区别：
def x(var):
    try:
        return int(var)
    except ValueError:
        print "No number!\n"
x("xyz")

def a(var):
    try:
        return int(var)
    except ValueError, aa:           # 参数类异常
        print "No number!\n", aa     # 发生异常提示参数
a("xyz")
'''
参数类异常不要忘记在ValueError后加上参数异常提示变量!!!!
'''