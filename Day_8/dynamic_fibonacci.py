# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 01:04:02 2020

@author: Arijit
"""

def fastFibo(num , memo):
    
    if num == 0 or num == 1:
        return 1
    else:
        try:
           return memo[num]
        except KeyError:
           result = fastFibo(num - 1 , memo) + fastFibo(num - 2 , memo)
           memo[num] = result
           return result