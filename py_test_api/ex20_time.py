"""
时间库
"""

import time
# 时间戳
# 时间戳表示的是从1970年1月1日00:00:00开始按秒计算的偏移量。我们运行“type(time.time())”，返回的是float类型。
t0 =  time.time() # 1742787563.5181856
print(t0) 

# 获取当前时间
t1 =  time.localtime() 
print(t1)
print(t1.tm_year)
print(t1.tm_mon)
print(t1.tm_mday)
print(time.strftime("%Y-%M-%d %H:%M:%S", t1)) # 格式化