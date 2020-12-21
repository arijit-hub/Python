# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 19:11:01 2020

@author: Arijit
"""

total_cost = 1000000
down_payment_percent = 0.25
down_payment = total_cost * down_payment_percent

investment_rate = 0.04
semi_annual_raise = 0.07
delta_difference = 100

starting_annual_salary = float(input('Enter your starting annual salary : '))

min_save_int = 0
max_save_int = 10000
best_prop_int = max_save_int

search_steps = 0
can_buy = True

while True:
    
    month = 0
    search_steps += 1
    current_savings = 0.0
    annual_salary = starting_annual_salary 
    best_prop = best_prop_int / 10000
    monthly_savings = (annual_salary / 12) * best_prop
    
    while month <= 36:
        month += 1
        current_savings = current_savings + ((current_savings) * investment_rate / 12) + monthly_savings
        if month % 6 == 0:
            annual_salary = annual_salary + (annual_salary) * semi_annual_raise 
            monthly_savings = (annual_salary / 12) * best_prop
    
    if abs(down_payment - current_savings) <= delta_difference:
        break
    if current_savings > down_payment:
        max_save_int = best_prop_int  
    else:
        min_save_int = best_prop_int  
        
    if min_save_int >= max_save_int:
        can_buy = False
        break
    
    best_prop_int = (max_save_int + min_save_int) // 2 
    
if can_buy:
    print('Best Saving Rate : ' , best_prop)
    print('Search steps : ' , search_steps)
else:
    print('Sorry! You can\'t buy that house')
    
