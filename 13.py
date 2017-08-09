# -*- coding:UTF-8 -*-

# Python 模块(Module)，是一个 Python 文件，以 .py 结尾，包含了 Python 对象定义和Python语句。
# 模块定义好后，我们可以使用 import 语句来引入模块，语法如下：
#                        import module1
# 调用模块时，必须这样引用：  模块名.函数名     如: time.localtime（）


# 一个模块只会被导入一次，不管你执行了多少次import。这样可以防止导入模块被一遍又一遍地执行。

# 当一个模块被导入到一个脚本，模块顶层部分的代码只会被执行一次。
# 如果你想重新执行模块里顶层部分的代码，可以用 reload() 函数。该函数会重新导入之前导入过的模块
# reload() 函数的格式：   reload(module_name)

"""
From...import 语句
       可以导入模块中的指定部分到当前命名空间中
From...import * 语句
       导入一个模块中所有项目
"""
import math
content = dir(math)     # dir()函数可以列出一个模块内所包含的所有变量，函数，定义模块
print content

def action(x):
    return lambda y: x + y
print (action(input("x=")))(input("y="))    # def函数中引用lambda
