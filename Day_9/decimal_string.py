# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 02:33:01 2021

@author: Arijit
"""

total = 0

dec_string = '1.23 , 1.54 , 2.34'

dec_num = dec_string.strip().split(',')

print(dec_num)

for num in dec_num:
    total = total + float(num)
    
print(total)