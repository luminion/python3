"""
方法
"""

class Student(object):
    numbers = 0
    def __init__(self, name = "noname", age = None):
        # 实例属性
        self.name = name
        self.age = age
        # 类属性
        Student.numbers += 1

    # 实例方法, 多一个默认参数self, 表示当前对象
    def study(self):
        print(self.name, "正在学习")
        
    # 类方法, 多一个默认参数cls, 表示当前类
    @classmethod
    def student_number(cls):
        print("当前类有",cls.numbers,"个学生")
    
    # 静态方法, 没有默认参数
    @staticmethod
    def print_info():
        print("这是一个学生类的静态方法")
        
    