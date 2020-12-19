# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 01:44:27 2020

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
    semi_annual_raise = float(input('Enter the semi-annual raise : '))
    
    month = 0
    while down_payment > current_savings:
        month += 1
        current_savings = current_savings + current_savings * (rate_of_interest/12) + monthly_savings
        if month % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_savings = (annual_salary / 12) * portion_saved
        print(month)
        print(monthly_savings)
        
    print(month)