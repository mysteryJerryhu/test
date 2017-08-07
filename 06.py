# -*- coding: utf-8 -*-
# 使用中文注释时，开头必须加上如上语句
for letter in 'python':
    print 'The letter is: ', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:
    print 'The fruit is: ', fruit
for index in range(len(fruits)):
    print 'Fruit is: ', fruits[index]
print "good bye!"

for num in range(10, 20):
    for i in range(2, num):
        if num % i == 0:
            j = num / i
            print '%d = %d * %d' % (num, i, j)
            break
    else:
        print num, 'is a prime'

rows = int(raw_input('array: '))
for i in range(0, rows):
    for k in range(0, 2 * rows - 1):
        if (i != rows - 1) and (k == rows - i - 1 or k == rows + i - 1):
            print "*",
        elif i == rows - 1:
            if k % 2 == 0:
                print "*",
            else:
                print " ",
        else:
            print " ",  # “,”号作用，python默认输出换行，“,”号可以手工控制不换行
    print "\n"    # \n 转义字符, 表示换行, 其他具体查询

arrays = [1, 8, 2, 6, 3, 9, 4]
for i in range(len(arrays)):
    for j in range(i + 1):
        if arrays[i] < arrays[j]:
            arrays[i], arrays[j] = arrays[j], arrays[i]
print arrays
