'''
Created on 2014年12月2日

@author: mengtao
'''

# 控制结构，while语句

number = 23;
running = True;

while running:
    guess = int(input('pleases enter an number!\n'));
    
    if guess == number:
        print('恭喜你，猜对了');
        running = False;
    elif guess < number :
        print('猜小了');
    else:
        print('猜大了');
    

