"""
集合
set 和 dict 类似，也是一组 key 的集合，但不存储 value。由于 key 不能重复，所以，在 set 中，没有重复的 key。

"""
s0 = set()  # 空集合
s1 = {1, 2, 3, 4, 5}  # 空集合, 只有key, 没有value

# 将元组转化为集合
t1 = (1, 2, 3, 4, 5)
s2 = set(t1)

l1 = [1, 2, 3, 4, 5]
s3 = set(l1)  # 列表转化为集合

# 不支持索引
# s1[0] # 报错

# 支持for循环
for item in s1:
    print(item)
