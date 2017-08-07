# -*- coding: utf-8 -*-
# 使用中文注释时，开头必须加上如上语句
numbers = [12, 37, 5, 42, 8, 3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print "even =", even, ",   odd =", odd

count = 0
while count < 9:
    print 'The count is: ', count
    count = count + 1
print "Good bye!"

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:
        continue
    print i

i = 1
while 1:
    print i
    i += 1
    if i > 10:
        break
