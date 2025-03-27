"""
字符串
python中单引号和双引号使用完全相同。
使用三引号(\'''或\""")可以指定一个多行字符串。

使用 '\'转义特殊字符
使用r""表示不转义

字符串可以用 + 运算符连接在一起，用 * 运算符重复。
Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
Python 中的字符串不能改变。
Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]

"""

# 空串
str0 = str()
# 单引号
str1 = 'hello'
# 双引号
str2 = "world"
# 三引号(单双引号都可), 使用三引号时, 可以定义一个多行字符串, 多行中的换行等符号都会被记录
str3 = """
hello
world"""
print(str3)

# 转义符\
str4 = "hello,\n world"
print(str4)

# 使用r""表示不转义
str5 = r"hello,\n world"
print(str5)

# 字符串乘法, 会将字符串重复指定的次数
print("---" + "你好" * 2)

print("=======================")
# 字符串索引,切片
str6= '123456789'
print(str6[0:-1])           # 输出第一个到倒数第二个的所有字符(不包含倒数第一个)
print(str6[0])              # 输出字符串第一个字符
print(str6[2:5])            # 输出从第三个开始到第六个的字符（不包含）
print(str6[2:])             # 输出从第三个开始后的所有字符
print(str6[1:5:2])          # 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str6[-1:10:-1])       # 倒序输出 
print(str6[::-1])           # 倒序输出, 简写 

# 字符串遍历, 字符串可以当作一个列表来处理, 支持for循环等列表的操作
for i in str6:
    print(i)

# 同时int, list tuple都可以转str
print("===========")
str7 =  str([1,2,3,4])
print(str7, type(str7)) # [1,2,3,4] <class 'str'>
str8 = str((1,))
print(str8, type(str8)) # (1,) <class 'str'>

# 常用方法
str9 = "hello world"
print(str9.count("0")) # 统计字符串中某个字符出现的次数
print(str9.find("0")) # 查找字符串中某个字符出现的位置, 找不到返回-1
print(str9.index("o",5)) # 查找字符串中某个字符出现的位置, 找不到报错, 从指定位置(5)开始查找
print(str9.strip()) # 去除空格
print(str9.replace("hello", "world")) # 替换字符串中的某个字符
print(str9.split("o"))  # 分割字符串
print("--".join(["123","456","789"])) 

print("================")

# 检查字符串是否只包含字母字符
"abc".isalpha()  # 返回 True
"abc123".isalpha()  # 返回 False，因为包含非字母字符

# 检查字符串是否只包含数字, 包括罗马数字等
"123".isdigit()  # 返回 True
"123.45".isdigit()  # 返回 false
"12AE".isdigit()  # 返回 false
"١٢٣٤٥".isdigit() # 阿拉伯数字, 可能输出: True, 根据环境和py版本不同, 输出结果可能不同

# 检查字符串是否只包含十进制数字字符
"123".isdecimal()  # 返回 True
"123.45".isdecimal()  # 返回 False，因为包含小数点

# 检查字符串是否只包含数字字符。与 isdecimal() 不同，isnumeric() 可以识别更多类型的数字，如罗马数字、分数
"123".isnumeric()  # 返回 True
"Ⅷ".isnumeric()  # 返回 True，因为是罗马数字

# 是否为空格
"   ".isspace()  # 返回 True
"  a  ".isspace()  # 返回 False，因为包含非空白字符


# 检查字符串是否是一个有效的 Python 标识符。有效的标识符由字母、数字和下划线组成，但不能以数字开头
"my_variable".isidentifier()  # 返回 True
"123variable".isidentifier()  # 返回 False，因为以数字开头

# 检查字符串是否只包含字母和数字字符
"abc123".isalnum()  # 返回 True
"abc 123".isalnum()  # 返回 False，因为包含空格



# 检查字符串中的所有字符是否都是 ASCII 字符。ASCII 字符的范围是从 0 到 127
"abc".isascii()  # 返回 True
"你好".isascii()  # 返回 False，因为包含非 ASCII 字符


# 检查字符串中的所有字符是否都是可打印字符。可打印字符包括字母、数字、标点符号、空格等，不包括控制字符（如换行符、制表符等）
"abc".isprintable()  # 返回 True
"abc\n".isprintable()  # 返回 False，因为包含换行符

