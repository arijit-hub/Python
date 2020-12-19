# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 02:04:35 2020

@author: Arijit
"""

annual_salary = float(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
monthly_savings = (annual_salary / 12) * portion_saved

total_cost = float(input('Enter the cost of your dream home: '))
portion_down_payment = 0.25 #25%
down_payment = total_cost * portion_down_payment

semi_annual_raise = float(input('Enter the semiannual raise, as a decimal: '))


annual_return = 0.04
current_savings = 0.0

number_of_months = 0

while current_savings < down_payment:
    current_savings += monthly_savings + ((current_savings * annual_return) / 12)
    number_of_months += 1
        
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_savings = (annual_salary / 12) * portion_saved
    
    print(number_of_months)
    print(monthly_savings)

print('Number of months: {}'.format(number_of_months))