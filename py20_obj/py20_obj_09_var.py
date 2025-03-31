"""
全局变量和局部变量
定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
在函数内部声明的变量只在函数内部的作用域中有效，调用函数时，这些内部变量会被加入到函数内部的作用域中，并且不会影响到函数外部的同名变量

全局变量：在函数外部定义的变量，可以在整个文件中被访问。在函数外部定义的变量对所有函数都是可见的，除非函数内部定义了同名的局部变量。
局部变量：在函数内部定义的变量，仅在函数内有效，函数外无法访问。局部变量优先级高于全局变量，因此如果局部变量和全局变量同名，函数内部会使用局部变量。

global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到 global 和 nonlocal 关键字了。
如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字了


"""

#!/usr/bin/python3

total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total

#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)


print("===========")
# 修改全局作用域
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num) # 123

print("=====")
# 修改嵌套作用域
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明, 指示此处修改的是外层函数的变量
        num = 100
        print(num)
    inner()
    print(num)
outer()