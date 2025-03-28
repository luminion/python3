"""
Python 提供了一些内置的装饰器，例如：
@staticmethod: 将方法定义为静态方法，不需要实例化类即可调用。
@classmethod: 将方法定义为类方法，第一个参数是类本身（通常命名为 cls）。
@property: 将方法转换为属性，使其可以像属性一样访问。
"""




# 内置的装饰器
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method.")

    @classmethod
    def class_method(cls):
        print(f"This is a class method of {cls.__name__}.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

# 使用
MyClass.static_method()
MyClass.class_method()

obj = MyClass()
obj.name = "Alice"
print(obj.name)

