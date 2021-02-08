# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 01:44:37 2021

@author: Arijit
"""
def findEven(L):
    '''
    Returns the first occurance of an even number in the list L.
    '''
    i = None
    
    for idx in range(len(L)):
        if L[idx] % 2 == 0:
            i = L[idx]
            break
    
    if i == None:
        raise ValueError('No even number is there!')
            
    print(i)