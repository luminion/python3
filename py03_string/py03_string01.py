"""
Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。
Python 访问子字符串，可以使用方括号 [] 来截取字符串，字符串的截取的语法格式如下：
变量[头下标:尾下标]
索引值以 0 为开始值，-1 为从末尾的开始位置。

Python中双引号和单引号使用完全相同。
使用三引号(\'''或\""")可以指定一个多行字符串。
三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。
一个典型的用例是，当你需要一块HTML或者SQL时，这时用字符串组合，特殊字符串转义将会非常的繁琐。

r-string 原始字符串
原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。
原始字符串除在字符串的第一个引号前加上字母 r（可以大小写）以外，与普通字符串有着几乎完全相同的语法。

f-string 格式化字符串
f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。
之前我们习惯用百分号 (%):

Unicode 字符串
在Python2中，普通字符串是以8位ASCII码进行存储的，而Unicode字符串则存储为16位unicode字符串，这样能够表示更多的字符集。使用的语法是在字符串前面加上前缀 u。

在Python3中，所有的字符串都是Unicode字符串。

"""

var1 = 'Hello World!'
var2 = "Runoob"
print ("var1[0]: ", var1[0])    # var1[0]:  H
print ("var2[1:5]: ", var2[1:5])    # var2[1:5]:  unoo

var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Runoob!') # 已更新字符串 :  Hello Runoob!

var3 = """第一行
第二行
第三行
"""
print(var3)


# 原始字符串
var4=r"\n你好\n你好"
print(var4)

# 格式化字符串
name = "小明"
age = 10
var5 = "我叫%s, 今年%d岁" % (name, age)
print(var5)
var6 = "我叫{name}, 今年{age}岁".format(name=name, age=age)
print(var6)
var7 = f"我叫{name}, 今年{age}岁"
print(var7)

var8 = u'20320' # 你 的unicode编码
print(var8)