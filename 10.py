# -*- coding:UTF-8 -*-
# 使用中文注释时，开头必须加上如上语句

# 二维列表
a = input("number of value：")  # 数值个数
b = input("number of list:")     # 列表个数
list_2d = [[0 for c in range(a)]for r in range(b)]      # 创建二维列表
list_2d[input("list No：")].append(input("value："))  # 向二维列表内添加数值
print list_2d                            # 所添加数值从每个列表最后向前推进

# 字典
Dict = {'Name': 'Zara', 'Age': 7}
print Dict
Dict['School'] = 'China University'   # 增加字典内容，一次一个，增加内容在字典头部
print Dict
Dict['Age'] = 8           # 更新字典某个键的值
print Dict
del Dict['name']          # 删除字典的某个键（值一同删除）
print Dict
Dict.clear()              # 清空字典的内容
print Dict
'''
字典有内置函数和方法，具体内容查询
字典的键只可以出现一次，出现多次，只记录最后一个值
键必须为不可变，故不可用列表作为键
'''
