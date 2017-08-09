# -*- coding:UTF-8 -*-

import os          # 导入os模块

# python文件读写
a = open("test.txt", "r+")          # a变量打开fo.txt,利用二进制打开只写  open()方法
a.write("I love Python!\nI love u!")     # 在fo.txt写入内容  write()方法
# 在“r+”模式时，写入和读取方法不可以同时使用，以下代码删除前后 ''' 后，将上述write()改为注释可使用
'''
x = a.read(10)                    # 文件的读取，这里读取10个字符内容  read()方法
print "read:", x
y = a.tell()                      # 告知文件读取当前位置 tell()方法
print "position:", y
'''
a.close()                         # 文件关闭  close()方法
print "file name:", a.name        # 返回文件名称
print "close:", a.closed          # 返回文件关闭状态，若关闭返回true，否则false
print "access mode:", a.mode      # 返回文件访问模式

# rename()和remove()方法需要导入os模块
os.rename("test2.txt", "abc.txt")  # 重命名test2.txt为abc.txt
os.remove("bbb.txt")               # 删除bbb.txt文件

'''
文件打开： varname = open(file name, access mode)  注意字符串形式
文件打开后注意关闭，不然无法再次进行操作
文件属性：.name    文件名称
         .closed  文件关闭状态
         .mode    文件访问模式
access mode(访问模式):
          r  只读
          w  只写
          a  追加
          b  以二进制打开
          +  读写，无文件时创建新文件读写
          r+ 打开一个文件用于读写。文件指针将会放在文件的开头
          w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
          a+ 打开一个文件用于读写。如果该文件已存在，指针则放在文件的结尾，打开模式为追加模
              式。如果该文件不存在，创建新文件用于读写。
          rb wb ab rb+ wb+ ab+ 原有基础上用二进制打开
文件、目录的相关方法具体查询
'''
