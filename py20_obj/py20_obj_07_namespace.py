"""
一般有三种命名空间：
内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

命名空间查找顺序:
假设我们要使用变量 runoob，则 Python 的查找顺序为：局部的命名空间 -> 全局命名空间 -> 内置命名空间。
如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常:



作用域
作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。

Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。
Python 的作用域一共有 4 种，分别是：
L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
G（Global）：当前脚本的最外层，比如当前模块的全局变量。
B（Built-in）： 包含了内建的变量/关键字等，最后被搜索。
LEGB 规则（Local, Enclosing, Global, Built-in）：Python 查找变量时的顺序是： L –> E –> G –> B。

Local：当前函数的局部作用域。
Enclosing：包含当前函数的外部函数的作用域（如果有嵌套函数）。
Global：当前模块的全局作用域。
Built-in：Python 内置的作用域。
在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。

"""

# var1 是全局名称
var1 = 5
def some_func():

    # var2 是局部名称
    var2 = 6
    def some_inner_func():

        # var3 是内嵌的局部名称
        var3 = 7