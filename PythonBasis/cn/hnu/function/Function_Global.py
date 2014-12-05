'''
Created on 2014年12月5日

@author: mengtao
'''

# global语句
def fun_global():
    global x;
    print('x的值为：', x);
    x = 20;
    print('改变后的x值为：', x);
    
x = 50;
fun_global();
print('x的最终值为：', x);
    