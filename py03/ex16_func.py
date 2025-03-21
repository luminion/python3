"""
函数

"""


# 定义一个函数
def func1():
    print("fun1")


# 调用函数
func1()


# 定义一个多参数函数
def func2(a, b):  # 形参
    print(a, b)


func2(1, 2)  # 实参


# 定义一个多参数函数, 并带默认参数
def func3(a, b="我是默认b", c= "我是默认c"):  # 带默认参数, 定义了该函数后, 不能再定义单参的函数
    print(a, b,c)

func3(1)  # 可以省略默认参数,
func3(1, "我不是默认")  # 可以修改默认参数
func3(1, c="jaj")  # 指定修改的默认参数是哪个

# 可变参数 可以传递多个参数, 使用*指定参数为可变参数, 可变参数会被封装为元组
def func4(*args):
    for i in args:
        print(i)
func4(1,2,3,4,5)
l1 = [1,2,3,4,5]
func4(*l1) # 拆包, 表示将列表中的元素作为参数传递给函数

# 关键字参数 允许传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def func5(**args):
    for key,value in args.items():
        print(key,value)
func5(name=1,age=2, hshs="张三") # 传递多个字典
d1 = {"first":1,"last":2}  
func5(**d1) # 拆包, 表示将字典中的元素作为参数传递给函数
