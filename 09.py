# -*- coding:UTF-8 -*-
# 使用中文注释时，开头必须加上如上语句

print "My name is %s and weight is %d kg!" % ('Zara', 21)  # 格式化输出, 注意 %()

List = ['physics', 'chemistry', 1997, 2000]

print List[-2]          # 读取倒数第二个

print "Value available at index 2: ", List[2]
List[2] = 2001
print "New value available at index 2: ", List[2]    # 列表的更新

print "The original value: ", List
del List[2]
print "After deleting value at index 2: ", List   # 列表的删除, 使用 del 语句

a = len(List)     # len()表示一个列表的长度值
print a
for x in List:
    print x,      # 迭代, 按照列表输出

# Python 列表函数
list1 = [56, 8, 79, 59]
list2 = [58, 26, 34, 68, 'dada', 'zda', 'bb']
seq = (156, 46846, 161)

a1 = cmp(list1, list2)   # 比较两个列表
a2 = max(list1)          # 获取列表内最大值
a3 = min(list2)          # 获取列表内最小值
a4 = list(seq)           # 将元组转换为列表
print '\n', a1
print a2
print a3
print a4

# Python 列表方法
list1.append(22)  # 在list1末尾添加22, 只允许一个值
xx1 = list1.pop(-1)    # 移除list1里最后一个值，并作为返回值
x2 = list1.count(8)    # 统计在list1内8出现的次数
x3 = list1.index(56)       # 查询list1里值56的位置
list1.reverse()          # 反向list1, 无法作为返回值
list2.extend([12, 35, 48])  # 在原列表末尾添加新的列表, 无法作为返回值
list2.remove(58)       # 移除list2里的58, 无法作为返回值
list2.insert(3, 88)      # 在list2的第3位插入88, 无法作为返回值
list2.sort()             # 将list2排序, 若有指定参数, 可按照指定参数排序, 无法作为返回值
# 完整列表排序方法: list.sort([func])
print xx1
print x2
print x3
print list1
print list2
