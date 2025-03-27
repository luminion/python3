"""
继承和多态

"""

class Teacher:
    pass

class Student(object):
    numbers = 0
    def __init__(self, name = "noname", age = None):
        # 实例属性
        self.name = name
        self.age = age
    def study(self):
        print(self.name,"正在学习")

class GoodStudent(Student):
    def __init__(self, name, age):
        super(GoodStudent, self).__init__(name, age)
    def study(self):
        print("好学生",self.name,"正在学习")
    
class BadStudent(Student):
    def __init__(self, name, age):
        super(BadStudent, self).__init__(name, age)
    def study(self):
        print("坏学生",self.name,"正在学习")

stu1 = Student("张三", 18)
stu2 = GoodStudent("李四", 19)
stu3 = BadStudent("王五", 20)
stu1.study()
stu2.study()
stu3.study()

## 多态, 调用传入对象的方法
def study(object):
    object.study()
    
study(stu1)
tea1 = Teacher()
study(tea1)# 报错, 因为该类没有方法