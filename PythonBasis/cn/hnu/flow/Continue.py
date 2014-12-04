'''
Created on 2014年12月4日

@author: mengtao
'''
# 控制结构，continue语句

while True:
    s = input('please enter an string!\n');
    if s == 'quit':
        break;
    if len(s) < 3 :
        continue;
    print('is over');
