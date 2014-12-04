'''
Created on 2014年12月4日

@author: mengtao
'''
# 局部变量

def fun_local(x):
    print('x的值为：', x);
    x = 2;
    print('改变后的x值为：', x);

x = 50;
fun_local(x);
print('x的最终值为：', x);
