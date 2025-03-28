"""
import 语句
想使用 Python 源文件，只需在另一个源文件里执行 import 语句，语法如下：
import module1, module2, ……
from module1 import func1, func2
from fibo import *

使用as取别名
import module1 as md , module2 as md2, ……
from module1 import func1 as f1, func2 as f2, ……
from module1 import *
"""

import py15_module02 as md1
from py15_module02 import func1 as f1
md1.func1()
f1()





