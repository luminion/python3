"""
函数

"""

# 全局变量
var1 = "张三"

def func1():
    var1 ="李四"
    print("func1内部",var1)

func1()
print(var1)

def func2():
    global var1 # 声明使用的是全局变量
    var1 = "王五"
    print("func2内部",var1)

func2()
print(var1)
