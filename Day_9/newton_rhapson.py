# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 00:56:35 2021

@author: Arijit
"""

## Finding root using newton_rapshon ##

num = int(input('Enter a number :'))

ans = num / 2.0

epsilon = 0.01


counter = 0

while abs(ans * ans - abs(num)) >= epsilon:
    print(ans)
    print('Step :' , counter + 1)
    ans = ans - ((ans * ans - abs(num))) / (2 * ans)
    counter += 1

if num < 0:
    ans = -ans
print('The square root of :' , num , 'is' , ans)