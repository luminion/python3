"""
turtle 库用于绘图


"""


def draw_time():
    import turtle
    import time
    turtle.showturtle() # 显示箭头
    turtle.backward(100) # 后退
    turtle.hideturtle()
    for i in range(100):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        turtle.clear()
        turtle.write(now,font=("Arial", 18, "normal"))
        time.sleep(1)
def draw_rectangle():
    import turtle
    import time
    turtle.showturtle()
    # turtle.speed(0)
    for e in range(100):
        turtle.forward(100)
        turtle.right(68)
    time.sleep(5)    

# 显示时间    
# draw_time()
# 绘制矩形
draw_rectangle()