"""
字典方法
dict.clear()        删除字典内所有元素
dict.fromkeys()     创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
dict.get(key, default=None) 返回指定键的值，如果键不在字典中返回 default 设置的默认值
key in dict     如果键在字典dict里返回true，否则返回false
dict.items()   以列表返回一个视图对象(EntrySet)
dict.setdefault(key, default=None)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
dict.update(dict2)  把字典dict2的键/值对更新到dict里
dict.values()       返回一个视图对象
dict.pop(key[,default]) 删除字典 key（键）所对应的值，返回被删除的值。
dict.popitem()  返回并删除字典中的最后一对键和值。
"""
