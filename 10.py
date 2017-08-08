# -*- coding:UTF-8 -*-
# 使用中文注释时，开头必须加上如上语句

# 二维列表
a = input("数值个数：")
b = input("列表数:")
list_2d = [[0 for c in range(a)]for r in range(b)]      # 创建二维列表
list_2d[input("输入列表序号：")].append(input("输入添加的数值："))  # 向二维列表内添加数值
print list_2d
