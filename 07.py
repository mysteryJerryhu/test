# -*- coding:UTF-8 -*-
# 使用中文注释时，开头必须加上如上语句
i = 2
while i < 100:
    j = 2
    while j <= (i / j):
        if not(i % j):
            break
        j = j + 1
    if j > i / j:
        print i, " is prime"
    i = i + 1                          # 双重循环嵌套

for letter in 'python':
    if letter == 'h':
        continue
    print 'The letter is ', letter     # continue 跳过条件，但不终止循环

var = 10
while var > 0:
    print 'The variable is ', var
    var = var - 1
    if var == 5:
        break                           # break 终止循环，后面循环语句不执行

for letter in 'python':
    if letter == 'h':
        pass                          # pass 不做任何运算, 仅仅作为占位, 用于后续开发
    print 'The letter is ', letter
