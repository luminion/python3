"""
魔法方法
是指以两个下划线开头和结尾的方法, 也称为特殊方法
是一种约定俗成的方法, 可以在特定的时机自动调用
"""
import threading
import time


class Student(object):
    # 构造函数, 创建对象时自动调用
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # tostring方法, str() 强转时调用
    def __str__(self):
        return "姓名:" + self.name + ", 年龄:" + str(self.age)
    # equals == 时调用
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    # 相加方法, + 运算符时调用
    def __add__(self, other):
        return Student(self.name, self.age + other.age)
    
stu1 = Student("张三", 18)
print(stu1) # 会自动调用__str__方法

# 创建线程 使用target 指定方法,  args 指定方法的参数
t1=  threading.Thread(target=print, args=("新线程打印",))
t1.start()

time.sleep(2)


