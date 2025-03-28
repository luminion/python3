"""
文件处理
使用open打开文件
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file: 文件路径
mode: 打开模式,默认为r,只读模式
buffering: 缓冲区大小,默认为-1,表示使用系统默认缓冲区
encoding: 编码方式,默认为None,表示使用系统默认编码

模式
r: 以只读模式打开文件，文件必须存在，若文件不存在会抛出 FileNotFoundError 异常
w: 以只写模式打开文件，若文件存在，会清空原有内容；若文件不存在，则创建新文件,只能写入文件内容，不能读取
a: 以追加模式打开文件，若文件存在，会在文件末尾追加内容；若文件不存在，则创建新文件, 只能写入文件内容，不能读取 

r+: 以读写模式打开文件，文件必须存在，若文件不存在会抛出 FileNotFoundError 异常,可以读取和写入文件内容，初始的文件指针位于文件开头
w+: 以读写模式打开文件，若文件存在，会清空原有内容；若文件不存在，则创建新文件
a+: 以读写模式打开文件，若文件存在，会在文件末尾追加内容；若文件不存在，则创建新文件,可以读取和写入文件内容，初始的文件指针位于文件末尾，若要读取内容，需要先移动文件指针

b : 二进制模式, 可以与上述模式组合操作


"""

file_name = "ex23_test.txt"

# 打开文件
def read_file():
    file = open(file_name,encoding="utf-8")
    text =  file.read()
    text8 =  file.read(8) # 读取8个字符
    line =  file.readline() # 读取一行
    lines =  file.readlines() # 读取所有行,返回一个列表
    
    print("读取到的文件内容:")
    print(text)
    file.close()

def write_file():
    file = open(file_name,mode="w",encoding="utf-8")
    text= input("请输入写入的内容\n")
    file.write(text)
    file.close() # 关闭文件, 此时文件才会被保存

def current_path():
    import os
    print(os.getcwd()) # 获取当前工作目录
    print(os.path.abspath(file_name)) # 获取文件的绝对路径
    os.close(0)


write_file()
read_file()
current_path()
# with 语句, 类似try-resource
with open(file_name,encoding="utf-8") as file:
    print(file.read())

