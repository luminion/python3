"""
字典
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：
d = {key1 : value1, key2 : value2 }
类似java中的hashmap
"""

# 定义
d1 ={
    "name":"张三",
    "age":18,
}
d2 = {} # 空字典

d3 = dict() # 空字典

d1["name"]= "李四" # 修改或添加

b = "name" in d1 # 判断key是否存在

# 遍历
for key,value in d1.items():
    print(key, value)
# 遍历key, 并根据key获取value
for key in d1:
    print(key, d1[key])

d1.pop("name") # 删除

d1.clear() # 清空
d1.get("name") # 获取value

d1.update({}) # 合并字典