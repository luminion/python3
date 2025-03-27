"""
类
格式
class 类名(继承的父类的集合):
其中父类的集合可以省略, 省略则默认继承object类

"""

class Student(object):
    pass # 空语句

tom = Student()
print(tom)
print(type(tom))
print(isinstance(tom, object))
print(isinstance(tom, Student))
