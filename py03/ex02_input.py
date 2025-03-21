"""
input()函数

"""

# input()函数, 会接收用户输入的内容, 并将内容作为字符串返回
age = input("输入变量值\n")
print("你输入的是",age)
print(type(age))
# print(age -10 ) # 报错, 字符串不能进行数学运算
# 类型转化
age = int(age)
print("输入数字减10 =", age-10)