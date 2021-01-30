# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 02:16:53 2021

@author: Arijit
"""

## Ask user for 10 numbers and get the highest odd number ##

user_inp = []
odd_list = []

for i in range(10):
    num_ins = int(input('Enter a number :'))
    user_inp.append(num_ins)
    if num_ins % 2 != 0:
        odd_list.append(num_ins)
    
if odd_list == []:
    print('You haven\'t entered any odd number!')
    
else:
    odd_list.sort()
    print(odd_list[-1])    
