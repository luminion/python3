"""
循环
for , while
语法同java
使用break, continue, pass跳过循环
其中pass是占位符, 什么都不做, 用于语法上的需要
"""

# while 循环
n = 0
while n < 5:
    print(n)
    n += 1

print("==================")

# for 循环
for n1 in [1, 2, 3, 4, 5]: # 重复列表中的元素
    print(n1)

print("========")
for n2 in range(5): # 重复5次
    print(n2)

print("========")
if True:
    pass  # 这里什么都不做，只是占位

def my_function():
    pass  # 函数体暂时为空

class MyClass:
    pass  # 类定义暂时为空