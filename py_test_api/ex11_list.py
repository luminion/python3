"""
序列
通用操作
len(item) 计算容器中元素个数
del(item) 删除元素
max(item) 返回容器中元素最大值, 如果是字典, 只针对key比较
min(item) 返回容器中元素最小值, 如果是字典, 只针对key比较

切片, 索引
"123456789"[::]  见字符串,除字符串外还支持列表, 元组

"""

# 创建列表, 列表内类型可以不同
list1 = ["张三",18,True]
print(list1)

# 将字符串转化为列表
list2 = list("张三")
print(list2)
print(len(list2))
print(min(list2))
print(max(list2))

# 列表可以相加, 实际为元素集合到一起
print(list1+list2)

# 列表遍历
print("=============")
# 元素遍历
for i in list1:
    print(i)
# 使用两个参数, 配合enumerate()函数,同时打印下标和元素, i为下标,j为元素
for i,j in enumerate(list1):
    print(i,j)
# 下标遍历
for i in range(len(list1)):
    print(list1[i])
    
# 元组, 不可变列表, 使用()声明
tuple1 = (1,2,3)
print(tuple1)
tuple2 = tuple() # 无元素的元组
tuple3 = (1,) # 单个元素的元组, 必须加,