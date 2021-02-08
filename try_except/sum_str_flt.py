# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 01:34:55 2021

@author: Arijit
"""

def sum_float_in_str(s):
    '''
    Return sum of the float values in the string s.
    '''
    total = 0
    
    for char in s:
        
        try:
            total = total + float(char)
            
        except ValueError:
            continue
        
    return total
        