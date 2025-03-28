"""

元组推导式（生成器表达式）
元组推导式可以利用 range 区间、元组、列表、字典和集合等数据类型，快速生成一个满足指定需求的元组。
元组推导式基本格式：
(expression for item in Sequence )
(expression for item in Sequence if conditional )

"""

a = (x for x in range(1,10))
print(a) # <generator object <genexpr> at 0x000001C120F05740> # 生成器对象
print(tuple(a)) # (1, 2, 3, 4, 5, 6, 7, 8, 9) # 可以直接将生成器对象转换成元组