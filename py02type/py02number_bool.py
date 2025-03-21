"""
Python3 支持 int、float、bool、complex（复数）。
在Python 3里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
像大多数语言一样，数值类型的赋值和计算都是很直观的。

注意：
Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， True==1、False==0 会返回 True，但可以通过 is 来判断类型。
在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。
"""

print("======================")
print(issubclass(bool, int))
# True
print(True == 1)
# True
print(False == 0)
# True
print(True + 1)
# 2
print(False + 1)
# 1


print("======================")
print(5 + 4)# 加法
print(4.3 - 2)# 减法
print(3 * 7)# 乘法
print(2 / 4)# 除法，得到一个浮点数
print(2 // 4)# 除法，得到一个整数
print(17 % 3)# 取余
print(2 ** 5)# 乘方
print(2.1+3) # 混合运算时, Python 会把整型转换成为浮点数





