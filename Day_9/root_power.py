# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 02:16:53 2021

@author: Arijit
"""

num = int(input('Please enter a number :'))

ans = 0

while ans**3 < abs(num):
    print(ans)
    ans = ans + 1

if ans ** 3 != abs(num):
    print('Sorry! The number doesn\'t have a cube root!!')
          
else:
    if num < 0:
        ans = -ans
    
    print('The cube root is :' , ans)
    