"""
模块
模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。模块可以被别的程序引入，以使用该模块中的函数等功能。
在import文件时, 若文件中存在流程性(没有定义为函数, 直接写逻辑)的代码, 则会被执行
"""

import ex17_var_range # 引入模块
ex17_var_range.func1() # 调用函数
a =  ex17_var_range.var1 # 调用变量
print(a) # 

print("====================")
from ex17_var_range import func1,var1 # 从模块中引入函数或变量
func1() # 调用函数

from ex17_var_range import func1 as func17 # 从模块中引入函数,并重命名
func17() # 调用函数

# 导入random模块
import random
print(random.randint(1,10)) # 随机数
print(random.choice([1,2,3,4,5,])) # 随机选择一个元素, 支持集合和字符串