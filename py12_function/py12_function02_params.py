"""
参数
以下是调用函数时可使用的正式参数类型：

必需参数
关键字参数
默认参数
不定长参数

必需参数
必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

关键字参数
关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

默认参数
调用函数时，如果没有传递参数，则会使用默认参数。

不定长参数
你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。
"""

def print_me( str ):
    print (str)
    return
# 调用 print_me 函数，不加参数会报错
print_me( "haha" )


def print_info( name, age ):
    "打印任何传入的字符串"
    print ("名字: ", name)
    print ("年龄: ", age)
    return
#使用关键字指定参数, 顺序可以不一致
print_info( age=50, name="runoob" )


def print_info2( name, age = 35 ):
    print ("名字: ", name)
    print ("年龄: ", age)
    return
# 使用默认参数, 可以不传递默认参数
print_info2("nihao")


# 加了 * 的参数会以元组(tuple)的形式导入
def print_info3( arg1, *vartuple ):
    print (arg1)
    print (vartuple)
# 不定长参数,不传递不定长的元组
print_info3( 10 ) 
# 不定长参数, 可以传递任意数量的参数, 
print_info3( 70, 60, 50 )

# 加了两个星号 ** 的参数会以字典的形式导入
def print_info4( arg1, **vartuple):
    print (arg1)
    print (vartuple)
# 不定长参数,不传递不定长
print_info4( 10 ) # 不传递不定长的元组
# 不定长参数, 可以传递任意数量的参数, 
print_info4( 70, name="tom",age=18 )

# 如果单独出现星号 *，则星号 * 后的参数必须用关键字传入
def f(a,b,*,c):
    return a+b+c
print(f(1,2,c=3)) # 6


