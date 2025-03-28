"""
类装饰器
除了函数装饰器，Python 还支持类装饰器。类装饰器是包含 __call__ 方法的类，它接受一个函数作为参数，并返回一个新的函数
"""

def my_decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def display(self):
            print("在类方法之前执行")
            self.wrapped.display()
            print("在类方法之后执行")
    return Wrapper

@my_decorator
class MyClass:
    def display(self):
        print("这是 MyClass 的 display 方法")

obj = MyClass()
obj.display()


