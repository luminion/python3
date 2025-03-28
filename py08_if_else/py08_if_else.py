"""
条件控制

if 嵌套
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句

"""


age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age -2)*5
    print("对应人类年龄: ", human)



print("=================")

def http_error(status):
    match status:
        case 400:
            # 即使没有 return 语句，Python 的 match case 结构也不会像其他语言的 switch 语句那样出现“穿透”情况，所以依然不需要 break
            print("Bad request")
        case 404:
            print("Not found")
        case 418:
            print("I'm a teapot")
        # 一个 case 也可以设置多个匹配条件，条件使用 ｜ 隔开，例如：
        case 500 | 501 | 502:
            print( "Server error") 
        # 兜底 case，类似于其他语言的 default 语句
        case _:
            return "Something's wrong with the internet"
msg =  http_error(400)
print(msg)
