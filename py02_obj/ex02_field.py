"""
类的属性

"""

class Student(object):
    def __init__(self):
        print("构造器函数")
    pass

# py中, 可以随时为变量添加属性
tom = Student()
tom.name = "张三"
tom.age = 18
tom.sex = "男"
print([tom.name, tom.age, tom.sex])
print(tom.__dict__) # 获取对象的所有属性

# py不支持构造器重载
class Student1(object):
    def __init__(self, name, age, sex):
        # 实例属性, 也就是对象属性
        self.name = name
        self.age = age
        self.sex = sex
        # 类属性, 也就是静态属性
        Student1.numbers = 100 
    pass

# py不支持构造器重载，但可以通过默认参数模拟
class Student2(object):
    def __init__(self, name=None, age=None, sex=None):
        self.name = name
        self.age = age
        self.sex = sex
# 使用不同数量的参数创建对象
tom = Student2("张三", 18, "男")
jack = Student2("李四")
print([tom.name, tom.age, tom.sex])
print([jack.name, jack.age, jack.sex])

# py不支持构造器重载，但可以通过 *args 和 **kwargs 模拟
class Student3(object):
    def __init__(self, *args, **kwargs):
        if args:
            self.name = args[0]
            if len(args) > 1:
                self.age = args[1]
            if len(args) > 2:
                self.sex = args[2]
        elif kwargs:
            self.name = kwargs.get('name')
            self.age = kwargs.get('age')
            self.sex = kwargs.get('sex')

# 使用不同方式创建对象
tom = Student3("张三", 18, "男")
jack = Student3(name="李四")
print([tom.name, tom.age, tom.sex])
print([jack.name, jack.age, jack.sex])