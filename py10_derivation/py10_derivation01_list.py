"""
列表推导式
[表达式 for 变量 in 列表] 或 [表达式 for 变量 in 列表 if 条件]
列表推导式格式为：
[out_exp_res for out_exp in input_list]
[out_exp_res for out_exp in input_list if condition]

out_exp_res：列表生成元素表达式，可以是有返回值的函数。
for out_exp in input_list：迭代 input_list 将 out_exp 传入到 out_exp_res 表达式中。
if condition：条件语句，可以过滤列表中不符合条件的值。

"""

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']
new_names = [name.upper()for name in names if len(name)>3]
print(new_names) # ['ALICE', 'JERRY', 'WENDY', 'SMITH']
