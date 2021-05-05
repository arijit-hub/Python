# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 02:05:46 2021

@author: Arijit
"""

def isIn(str1 , str2):
    if (str1 in str2) or (str2 in str1):
        print('Yes! They are similar!')
    else:
        print('No! They are not similar!')