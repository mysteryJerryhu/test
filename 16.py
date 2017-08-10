# -*- coding:UTF-8 -*-

# 异常处理2
"""
   try:
      运行语句
   finally:
      发生异常后退出try的语句
# try:...finally:.. 语句
无论是否发生异常都执行finally语句
"""
try:
    a = open("mm.txt", "w")
    a.write("It's a test file!!")
finally:
    print "Error:No file find or read fail!!"
