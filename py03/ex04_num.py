"""
数字类型

在python中,数字类型分为整型和浮点型
整型: 整数, 例如: 1, 2, 3, 4, 5, 6, 7, 8, 9, 0 
浮点型: 小数, 例如: 1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 0.0

在python中, 小整数池: [-5, 256]
在该范围内的对象都是相等的, 类似java中的-128至127

可以使用id()函数来查看对象的内存地址

"""
import math

f1 = 0.23232
f2= 3
f3 = f2-f1
print(f3) # 可能会有精度问题
f4 = round(f3,2) # 四舍五入,保留2位小数
print(f4)
n5 = math.ceil(f4) # 向上取整
print(n5)
n6 = math.floor(f4) 
print(n6) # 向下取整
n7 = 10%3
print(n7) # 取余数


# 查看内存地址, 使用命令行, 不能使用pycharm,pycharm有优化, 可能会相同地址
n1,n2,n3,n4 = 10,10,3000,3000
print(id(n1))
print(id(n2))
print(id(n3))
print(id(n4))

