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

# 匿名函数lambda 
lam1 = lambda a:a+1 # 一个参数
print(lam1(3))
lam2 = lambda a,b:a+b # 两个参数
print(lam2(3,4))

# map函数, 指定一个处理的函数, 再指定一个数据集(可迭代的),数据集中的每个元素都会被处理函数处理后返回一个map对象
result =  map(lambda a:a+1,[1,2,3,4,5]) # 使用lambda匿名函数, 对列表中的每个元素加1
print(result)
print(list(result)) # 转化为list

from functools import reduce
# reduce函数, 指定一个处理的函数, 再指定一个数据集(可迭代的),数据集中的每个元素都会被处理函数处理后返回一个值
result =  reduce(lambda a,b:a+b,[1,2,3,4,5]) # 使用lambda匿名函数, 对列表中的每个元素加1
print(result)

result = filter(lambda a:a%2==0,[1,2,3,4,5]) # 使用lambda匿名函数, 判断是否为偶数
print(list(result)) # 转化为list

# 内置函数=====================
eval("print(\"hello eval===========\")") # 执行字符串中的python代码, 返回执行结果
exec("print(\"hello eval===========\")") # 执行字符串中的python代码, 不返回执行结果
globals()  # 返回全局变量


dir([1,2,3,4,5])# 返回对象的所有属性和方法
help([1,2,3,4,5])# 接收一个对象, 更详细的返回对象的所有属性和方法
isinstance([1,2,3,4,5],list) # 判断是否为指定类型
type([1,2,3,4,5]) # 返回对象的类型
id("11") # 返回对象的内存地址



abs(-1) # 绝对值
all([1,2,3,4,5]) # 判断是否所有元素都为True
any([1,2,3,4,5]) # 判断是否有一个元素为True
max(1,2,3,4,5) # 最大值
divmod(100,10) # 除法, 返回商和余数, 返回的第一个元素是商, 第二个元素是余数
pow(2,3) # 幂运算, 2的3次方
round(1.23456,2) # 保留小数点后2位
range(1,10) # 生成一个从1到9的数列


bin(10) # 十进制转二进制
oct(10) # 十进制转八进制
hex(10) # 十进制转十六进制
chr(65) # 十进制转字符
ord("A") # 字符转十进制ascii码






