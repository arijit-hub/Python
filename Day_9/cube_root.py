# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 02:50:05 2021

@author: Arijit
"""

## Finding cube with bisection search ##

num = int(input('Enter a number :'))

epsilon = 0.01

low = min(-abs(num) , -1)
high = max(1.0 , abs(num))
ans = (high + low) / 2

while abs(ans ** 3 - abs(num)) >= epsilon:
    print('Ans :' , ans , ' Low :'  , low , 'High :' , high)
    if abs(ans ** 3) > abs(num):
        high = ans
    else:
        low = ans
    ans = (high + low) / 2
    

if num < 0:
    neg_ans = -ans
    print('Cube roots are :' , neg_ans)

else:
    print('Cube roots are :' , ans)

