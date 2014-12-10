'''
Created on 2014年12月10日

@author: mengtao
'''

# 使用sys模块

import sys;

print('The command line arguments are:');
for i in sys.argv:
    print(i);
print('The PYTHONPATH is', sys.path, '\n');