# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 00:25:06 2020

@author: Arijit
"""

def lets_buy_house():
    
    total_cost = float(input('Enter the cost of your dream house : '))
    portion_down_payment = 0.25
    down_payment = total_cost * portion_down_payment
    current_savings = 0.0
    rate_of_interest = 0.04
    annual_salary = float(input('Enter your annual salary : '))
    monthly_salary = annual_salary / 12
    portion_saved = float(input('Portion of the monthly salary to be saved : '))
    monthly_savings = monthly_salary * portion_saved
    
    month = 0
    while down_payment > current_savings:
        month += 1
        current_savings = current_savings + current_savings * (rate_of_interest/12)
        current_savings += monthly_savings
        
    print(month)