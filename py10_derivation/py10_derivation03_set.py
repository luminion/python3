"""
set集合推导式
集合推导式基本格式：
{ expression for item in Sequence }
{ expression for item in Sequence if conditional }

"""


setnew = {i**2 for i in (1,2,3)}
print(setnew) # {1, 4, 9}
