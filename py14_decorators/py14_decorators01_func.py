"""
装饰器（decorators）是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为
装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数

装饰器的语法使用 @decorator_name 来应用在函数或方法上。

Python 还提供了一些内置的装饰器，比如 @staticmethod 和 @classmethod，用于定义静态方法和类方法。

装饰器的应用场景：

日志记录: 装饰器可用于记录函数的调用信息、参数和返回值。
性能分析: 可以使用装饰器来测量函数的执行时间。
权限控制: 装饰器可用于限制对某些函数的访问权限。
缓存: 装饰器可用于实现函数结果的缓存，以提高性能。
"""

# 示例
def my_decorator(func):
    def wrapper():
        print("在原函数之前执行")
        func()
        print("在原函数之后执行")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
    

say_hello() # 此时执行时, 实际执行的是my_decorator(), say_hello()被作为参数传递给my_decorator()函数 

# 带参数的装饰器
# 如果原函数需要参数，可以在装饰器的 wrapper 函数中传递参数
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("在原函数之前执行")
        func(*args, **kwargs)
        print("在原函数之后执行")
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")


# 装饰器本身也可以接受参数，此时需要额外定义一个外层函数
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func(*args, **kwargs)
        return wrapper
    return decorator
# repeat 函数是一个装饰器工厂，它接受一个参数 num_times，返回一个装饰器 decorator。
# decorator 接受一个函数 func，并返回一个 wrapper 函数。
# wrapper 函数会调用 func 函数 num_times 次。
# 使用 @repeat(3) 装饰say_hello 函数后，调用 say_hello 会打印 "Hello!" 三次。
@repeat(3)
def say_hello():
    print("Hello!")
say_hello()

