"""
类型转化

int(x, [基数]) 将x转换为一个整数,如果x为浮点数,则截断小数部分,基数表示几进制
float(x) 将x转换为一个浮点数
bool(x) 将x转换为一个布尔值
str(x) 将对象x转换为字符串
"""

str1 = "123.123"
print(float(str1))

print(bool(0.0)) # False
print(bool(0.1)) # True
print(bool("False")) # True , 非空字符串为True