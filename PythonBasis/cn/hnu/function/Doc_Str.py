'''
Created on 2014年12月10日

@author: mengtao
'''

# DocStrings

def fun_prinMax(x, y):
    '''Prints the maximum of two numbers.
    The two values must be integers.'''
    x = int(x);
    y = int(y);
    
    if x > y:
        print (x, 'is maximum');
    else:
        print (y, 'is maximum');
        
fun_prinMax(3, 5);
    
    