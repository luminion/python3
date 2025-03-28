"""
字典
字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 key=>value 对用冒号 : 分割，每个对之间用逗号(,)分割，整个字典包括在花括号 {} 中 
注意：dict 作为 Python 的关键字和内置函数，变量名不建议命名为 dict。
键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字, 元组。
"""

# 创建空字典
empty_dict = {}
empty_dict2 = dict()

# 创建字段
tinydict = {'name': 'runoob', 'likes': 123, 'url': 'www.runoob.com'}
print ("tinydict['Name']: ", tinydict['name'])
print ("tinydict['Age']: ", tinydict['likes'])

# 修改字典
tinydict['likes'] = 8               # 更新 Age
tinydict['url'] = "菜鸟教程"  # 添加信息

# 删除
del tinydict['name'] # 删除键 'Name'
tinydict.clear()     # 清空字典

# 构造函数 dict() 直接从键值对元组列表中构建字典。如果有固定的模式，列表推导式指定特定的键值对
dict11 =  dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict11)

# 字典推导可以用来创建任意键和值的表达式词典
dict12 = {x: x**2 for x in (2, 4, 6)}
print(dict12) # {2: 4, 4: 16, 6: 36}

# 在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
    
# 同时遍历两个或更多的序列，可以使用 zip() 组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    
# 要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值：
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

