'''
Created on 2014年12月2日

@author: mengtao
'''

# 控制结构 if语句

number = 23;
guess = int(input('please enter an number!\n'));

if guess == number:
    print('恭喜你答对了');
elif guess < number:
    print('猜小了');
else:
    print('猜大了');


