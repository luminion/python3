"""
try except
"""
# 语法结构
try:
    a = 10
    b = 0
    # a/b
    print("执行完成")
    raise Exception("手动抛出异常") # 手动抛出异常
except ZeroDivisionError as e:
    print("除0异常:", e)
else:
    print("else") # 没有异常时执行
finally:
    print("finally") # 无论是否有异常都会执行