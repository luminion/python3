"""
Python 中的循环语句有 for 和 while。
"""

n = 100
sum1 = 0
counter = 1
while counter <= n:
    sum1 = sum1 + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n, sum1))


# for 循环可以遍历任何可迭代对象，如一个列表或者一个字符串
for letter in 'Python':
    print(letter)



# 当循环执行完毕（即遍历完 iterable 中的所有元素）后，会执行 else 子句中的代码，如果在循环过程中遇到了 break 语句，则会中断循环，此时不会执行 else 子句
sites = ["Baidu", "Google","Runoob","Taobao"]
for site in sites:
    if site == "Taobao":
        print("跳过")
        continue
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")

# range() 函数
# 生成指定区间的值
range(5,9)
