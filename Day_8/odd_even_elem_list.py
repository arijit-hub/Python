# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 23:58:07 2020

@author: Arijit
"""

def even(num):
    return num % 2 == 0

def separate_odd_even(input_list):
    odd_list = []
    even_list = []

    for i in range(len(input_list)):
        if even(input_list[i]):
            even_list.append(input_list[i])
        else:
            odd_list.append(input_list[i])
            
    return odd_list , even_list