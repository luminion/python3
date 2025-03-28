"""
将列表当做栈使用
在 Python 中，可以使用列表（list）来实现栈的功能。
栈是一种后进先出（LIFO, Last-In-First-Out）数据结构，意味着最后添加的元素最先被移除。
列表提供了一些方法，使其非常适合用于栈操作，特别是 append() 和 pop() 方法。
用 append() 方法可以把一个元素添加到栈顶，用不指定索引的 pop() 方法可以把一个元素从栈顶释放出来。

栈操作
压入（Push）: 将一个元素添加到栈的顶端。
弹出（Pop）: 移除并返回栈顶元素。
查看栈顶元素（Peek/Top）: 返回栈顶元素而不移除它。
检查是否为空（IsEmpty）: 检查栈是否为空。
获取栈的大小（Size）: 获取栈中元素的数量。
以下是如何在 Python 中使用列表实现这些操作的详细说明：
"""

stack1 = [1, 2, 3]
print(stack1)  # 输出: [1, 2, 3]
top_element = stack1.pop()
print(top_element)  # 输出: 3
stack1.append(4) # 压入4
top_element= stack1.pop()
print(top_element) # 输出: 4

