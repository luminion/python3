"""
Python 语言支持以下类型的运算符:

算术运算符
比较（关系）运算符
赋值运算符
逻辑运算符
位运算符
成员运算符
身份运算符

Python运算符优先级
以下表格列出了从最高到最低优先级的所有运算符， 相同单元格内的运算符具有相同优先级。 
运算符均指二元运算，除非特别指出。 相同单元格内的运算符从左至右分组（除了幂运算是从右至左分组）：
(expressions...),[expressions...], {key: value...}, {expressions...}    圆括号的表达式
x[index], x[index:index], x(arguments...), x.attribute                  读取，切片，调用，属性引用
await x                                                                 await 表达式
**                                                                      乘方(指数)
+x, -x, ~x                                                              正，负，按位非 NOT
*, @, /, //, %                                                          乘，矩阵乘，除，整除，取余
+, -                                                                    加和减
<<, >>                                                                  移位
&                                                                       按位与 AND
^                                                                       按位异或 XOR
|                                                                       按位或 OR
in,not in, is,is not, <, <=, >, >=, !=, ==                              比较运算，包括成员检测和标识号检测
not x                                                                   逻辑非 NOT
and                                                                     逻辑与 AND
or                                                                      逻辑或 OR
if -- else                                                              条件表达式
lambda                                                                  lambda 表达式
:=                                                                      赋值表达式
"""
#!/usr/bin/python3

a = 20
b = 10
c = 15
d = 5
e = 0

e = (a + b) * c / d       #( 30 * 15 ) / 5
print ("(a + b) * c / d 运算结果为：",  e)

e = ((a + b) * c) / d     # (30 * 15 ) / 5
print ("((a + b) * c) / d 运算结果为：",  e)

e = (a + b) * (c / d)    # (30) * (15/5)
print ("(a + b) * (c / d) 运算结果为：",  e)

e = a + (b * c) / d      #  20 + (150/5)
print ("a + (b * c) / d 运算结果为：",  e)

print("===========")
# and 拥有更高优先级:
x = True
y = False
z = False

if x or y and z:
    print("yes")
else:
    print("no")
# 以上实例先计算 y and z 并返回 False ，然后 x or False 返回 True，输出yes