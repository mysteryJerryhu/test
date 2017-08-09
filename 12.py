# -*- coding:UTF-8 -*-
# 使用中文注释时，开头必须加上如上语句

# 一个简单的查看日历函数
# 函数基本格式 def functionname(parameters):       定义函数名，变量，变量数
#                function_suite                  函数表达式（函数体）
#                return[expression]              函数返回值

def date():
    import calendar
    import time
    a = input("Enter year(after 1970)：")
    b = input("Enter month：")
    cal1 = calendar.month(a, b)
    print cal1, "Localtime：", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return
date()

def printinfo(name, age):
    print "Name:", name
    print "Age:", age
    return                            # 关键字顺序不重要
printinfo(age=50, name="mike")

def info(arg1, *vartuple):
    print "输出:"
    print arg1
    for var in vartuple:           # 不定长参数,可以不指定变量 def(formal_args, *var_args)
        print var
    return
info(10)
info(70, 60, 50)

Sum = lambda arg1, arg2: arg1 + arg2   # 匿名函数表达式：lambda arg: expression
print "Addition value:", Sum(10, 20)
'''
函数内部的变量称作局部变量，局部变量只参与函数内部运算，不影响整体
函数外部变量称作全局变量，影响整个程序
当函数内部需要使用全局变量时，可以在内部引用时，在变量前加上: global, global可以同时定义多个变量
'''