"""
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。
"""
# 创建列表
list1 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
list2 = ['1', '2', '3']

# 长度
len(list1)

# 拼接
list3 = list1 + list2

# 重复
list4 =  ['Hi!'] * 4	 # ['Hi!', 'Hi!', 'Hi!', 'Hi!']

# 元素是否存在于列表中
"red" in list1	 # True

# 迭代
for x in list3: print(x)

# 截取和拼串

L=['Google', 'Runoob', 'Taobao']
# 'Taobao'	读取第三个元素
print(L[2])
# 'Runoob'	从右侧开始读取倒数第二个元素: count from the right
print(L[-2])
# ['Runoob', 'Taobao']	输出从第二个元素开始后的所有元素
print(L[1:])

# 比较
# 列表比较需要引入 operator 模块的 eq 方法
import operator
a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))