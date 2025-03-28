"""
print() 函数
方法签名
def print(*values: object,
          sep: str | None = " ",
          end: str | None = "\n",
          file: SupportsWrite[str] | None = None,
          flush: Literal[False] = False) -> None
)
"""
# 打印字符串
print("你好") 
# 输出数字
print(11111) 
# 输出变量
age = 18
print(age) 
# 打印多个内容时, 可以使用','进行链接,链接时会使用sep进行分隔, 默认为空格
print("我今年",18,"岁")
# 使用sep指定分隔符, 替换默认的空格
print("我今年",18,"岁", sep="---")
# 使用end指定结束符, 替换默认的换行
print("我今年",18,"岁", end="\n\n") 
# 格式化输出 ,%s字符串, %d有符号的十进制整数(如%06d, 6位整数,前补0), %f浮点数($.2f, 表示小数点保留2位), %%输出%自身
print("我今年%d岁" % 18)
print("我今年%04d岁" % 18)
print("我今年%d岁, 我叫%s, 我是%s" % (18, "张三", "男"))
