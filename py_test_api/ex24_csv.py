"""
读取csv文件
csv文件是一种常见的文件格式，它使用特定的分隔符（如逗号）将数据分隔成行和列。

"""
import csv

# 需要指定字符集为utf-8, 否则会出现乱码
with open('ex24_test.csv', 'r',encoding="utf-8") as file:
    reader = csv.reader(file)
    head = next(reader) # 获取表头, 获取后遍历时会跳过表头 若在遍历完后再获取会报错
    ages = []
    print("============")
    for row in reader:
        # 实际上每一行都是一个 集合 [] , 可以用下标访问对应的元素
        print(row) # 遍历
        ages.append(int(row[1])) # 获取第二列的年龄
    print("============")
    print(ages)
# 指定新行为空串, 否则写入时会自动添加换行,多出空行
with open('ex24_test.csv', 'a+',encoding="utf-8", newline="") as file:
    # 写入数据
    writer =  csv.writer(file)
    writer.writerow(["baby","3","100"])
    writer.writerows([["baby","4","100"],["baby","5","99"]])
    print("==========")
    
    

    