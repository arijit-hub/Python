# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 01:48:22 2021

@author: Arijit
"""

from itertools import permutations

def finding_all_permutation(max_idx):
    '''
    Finds all the permutations given a range of numbers with the max value of max_idx.
    '''
    all_permutations = list(permutations(range(1 , max_idx + 1)))
    
    return all_permutations

