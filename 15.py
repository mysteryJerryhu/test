# -*- coding:UTF-8 -*-

# 异常处理1
"""
异常处理：
      try:
        运行代码                                   # 程序基本运行
      except <异常种类1,异常种类2,异常种类3....>:
         发生上述一种异常后的提示及处理               # 注意只有一种异常可处理,多种处理可使用多
      else:                                          个 except <异常>： 语句
         未发生异常的提示及处理

# 基本异常处理格式,异常种类具体查询
"""

try:
    fh = open("IOtest.txt", "w")
    fh.write("It's a test file for test exceptional!!")
except IOError:
    print "Error: No file find or read fail!!"
else:
    print "Write successfully!!"
    fh.close()
'''
该测试可先将IOtest.txt权限修改为只读，进行异常测试
IOtest.txt文件权限去掉只读时，写入成功
'''
