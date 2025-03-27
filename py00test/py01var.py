"""
Python 中的变量不需要声明。每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
在 Python 中，变量就是变量，它没有类型，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值

多个变量赋值
Python允许你同时为多个变量赋值。例如：
a = b = c = 1
以上实例，创建一个整型对象，值为 1，从后向前赋值，三个变量被赋予相同的数值。
您也可以为多个对象指定多个变量。例如：
a, b, c = 1, 2, "runoob"
以上实例，两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。

Python3 中常见的数据类型有：
Number（数字）
String（字符串）
bool（布尔类型）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
Python3 的六个标准数据类型中：
不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
此外还有一些高级的数据类型，如: 字节数组类型(bytes)。

"""

counter = 100          # 整型变量
miles   = 1000.0       # 浮点型变量
name    = "runoob"     # 字符串
print (counter)
print (miles)
print (name)

print("===========================")
# 多个变量赋值
a, b, c = 1, 2, "runoob"
d ,e = "runoob", a
print(a)
print(b)
print(c)

"""
内置的 type() 函数可以用来查询变量所指的对象类型。
此外还可以用 isinstance() 来判断
isinstance 和 type 的区别在于：
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。
"""

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d)) # <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
print(isinstance(a, int)) # True



print("=============")
# 使用is 比较两个对象是否为同一个对象
print(a is b) # False
print(d is a) # False
print(e is a) # True

# 使用del 删除变量
del a,
# del a,b,c # 报错(a已经被删除)
# print(a) # 报错

"""
注意：
1、Python可以同时为多个变量赋值，如a, b = 1, 2。
2、一个变量可以通过赋值指向不同类型的对象。
3、数值的除法包含两个运算符：/ 返回一个浮点数，// 返回一个整数。
4、在混合计算时，Python会把整型转换成为浮点数。
"""