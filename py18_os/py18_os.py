"""
Python3 OS 文件/目录方法
os 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示
os.access(path, mode)       检验权限模式
os.chdir(path)              改变当前工作目录
os.chflags(path, flags)     设置路径的标记为数字标记。  
os.chmod(path, mode)        更改权限模式
os.chown(path, uid, gid)    更改所有权
os.chroot(path)             改变当前进程的根目录
os.close(fd)                关闭文件描述符
os.closerange(fd_low, fd_high)  关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
os.dup(fd)                  复制文件描述符 fd
os.dup2(fd, fd2)            将一个文件描述符 fd 复制到另一个 fd2
os.fchdir(fd)               通过文件描述符改变当前工作目录	
os.fchmod(fd, mode)         改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限
os.fchown(fd, uid, gid)     修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
...
https://www.runoob.com/python3/python3-os-file-methods.html




"""


