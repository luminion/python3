r"""
Python 转义字符
在需要在字符中使用特殊字符时，python 用反斜杠 \ 转义字符。如下表：
\(在行尾时)	续行符, 表示下面行内容依然在本行
\a	    响铃, 执行后电脑有铃声
\b	    退格(Backspace)
\000	空
\v	    纵向制表符, 换行+tab
\t	    横向制表符, 也就是tab键
\r	    回车，将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
\f	    换页
\yyy	八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
\xyy	十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
"""

print('\'Hello, world!\'')  # 输出：'Hello, world!'

print("Hello, world!\nHow are you?")  
# 输出：Hello, world!
#       How are you?

print("Hello, world!\tHow are you?")  
# 输出：Hello, world!    How are you?

print("Hello,\b world!")  # 输出：Hello world!

print("Hello,\f world!")  # 输出：
# Hello,
#  world!

print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65

print("\x41 为 A 的 ASCII 代码")  # 输出：A 为 A 的 ASCII 代码

decimal_number = 42
binary_number = bin(decimal_number)  # 十进制转换为二进制
print('转换为二进制:', binary_number)  # 转换为二进制: 0b101010

octal_number = oct(decimal_number)  # 十进制转换为八进制
print('转换为八进制:', octal_number)  # 转换为八进制: 0o52

hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
print('转换为十六进制:', hexadecimal_number) # 转换为十六进制: 0x2a


import time
# 使用\r 实现百分比进度
for i in range(101):
    print("\r{:3}%".format(i),end=' ')
    time.sleep(0.05)
