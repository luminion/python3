"""
变量
Python3 中常见的数据类型有：
Number（数字）
String（字符串）
bool（布尔类型）
List（列表, 元素集合）
Tuple（元组, 类似列表, 但不可变）
Set（集合, 无序且不重复的元素集合）
Dictionary（字典, key, value键值对）
Python3 的六个标准数据类型中：
不可变数据（4 个）：Number（数字）、String（字符串）、Tuple（元组)、bool（布尔类型）； 
可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
此外还有一些高级的数据类型，如: 字节数组类型(bytes)。

在python中, 不存在常量, 可以通过约定俗成的方式, 来表示常量, 例如纯大写
在python中, 变量自身没有类型, 可以随时修改不同类型的值

type()函数, 查看变量类型
isinstance()函数, 判断变量是否为某一类型

"""
name = "张三" # 声明字符串
print(type(name), name) 
# 多个变量赋值, 可以不同类型混合, 按顺序对应
a, b, c, var1 = 1, 2, 3, "字符串"
# 相同值变量赋值
d = e = f = 4
# 可以将变量修改为不同类型
name = 1111
print(type(name), name) 
print(isinstance(name, int))

