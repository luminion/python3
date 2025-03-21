"""
条件分支
使用if,下级代码块通过缩进控制, 缩进任意空格数量都行,但要保持一致

"""
name = "张三"
age = 18
if name == "张三":
    print("张三, 你好")
    # 嵌套if
    if age==18:
        print("18岁")
    else:
        print("不是18岁")
elif name == "李四":
    print("李四, 你好")
else:
    print("陌生人, 你好")
    
# 类似swatch case, 会依次匹配所有case, 直到匹配到一个case 
match age:
    case 18:
        print("18岁")
    case 20:
        print("20岁")
    case _:
        print("其他")
    