'''
Created on 2014年11月30日

@author: mengtao
'''

# _init_.py的作用有如下几点：
# 1. 相当于class中的def __init__(self):函数，用来初始化模块。
# 2. 把所在目录当作一个package处理
# 3. from-import 语句导入子包时需要用到它。 如果没有用到, 他们可以是空文件。
# 如引入package.module下的所有模块  from package.module import * 
# 这样的语句会导入哪些文件取决于操作系统的文件系统. 所以我们在_init_.py 中加入 _all_变量. 
# 该变量包含执行这样的语句时应该导入的模块的名字. 它由一个模块名字符串列表组成.