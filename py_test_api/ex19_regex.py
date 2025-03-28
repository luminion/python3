"""
正则表达式
py中对应正则的库为re
"""
# 导入库
import re
res = re.match("hello", "hello world")
print(res) # <re.Match object; span=(0, 5), match='hello'>
print(bool(res)) # True