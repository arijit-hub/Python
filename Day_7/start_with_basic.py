# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 23:21:30 2020

@author: Arijit
"""
import math

def mit_1():
    
    x = int(input("Enter number x : "))
    y = int(input("Enter number y : "))
    power = x ** y
    print("x ** y = " , power)
    logarithm = math.log2(power)
    print("log(x) = " , logarithm)