"""
Python3 错误和异常

Python 有两种错误很容易辨认：语法错误和异常。
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常
"""

# 异常处理
try:
    0/(1-1)
    # f = open('myfile.txt')
    # s = f.readline()
    # i = int(s.strip())
    # raise Exception('x 不能大于 5。x 的值为: {}'.format(x)) # 手动抛出异常
except OSError as err:
    print("OS error: {0}".format(err))
except (ValueError, RuntimeError): # 处理多个异常
    raise # 抛出当前异常
else:
    print("else") # 没有异常时执行
finally:
    print("finally") # 无论是否有异常都会执行
    
