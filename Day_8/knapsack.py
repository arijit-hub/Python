# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 15:31:34 2020

@author: Arijit
"""

class Food(object):
    '''
    Defines the data-type food.
    '''
    def __init__(self , value , weight):
        self.value = value
        self.weight = weight
    
    def __str__(self):
        return '<' + str(self.value) + ',' + str(self.weight) + '>'
    
    
    def getValue(self): #getter for value
        return self.value
    
    def getWeight(self): #getter for weight
        return self.weight
    
    def getDensity(self): #getter for density
        return self.getValue() / self.getWeight()
    

#Lets create a menu for the food to choose for the knapsack
def create_menu():
    num_items = int(input('How many elements do you want to enter?'))
    itemList = []
    for i in range(num_items):
        input_food = Food(int(input('Enter a food value : ')) , int(input('Enter food weight : ')))
        itemList.append(input_food)
    return itemList

def knapsack_problem(items , constraint , keyFunction):
    '''
    Function to solve the knapsack problem
    '''
    sortedItems = sorted(items , key = keyFunction , reverse = True)
    totalValue = 0.0
    totalWeight = 0.0
    
    for i in range(len(sortedItems)):
        if ((totalWeight + sortedItems[i].getWeight()) < constraint):
            totalValue = totalValue + sortedItems[i].getValue()
            totalWeight = totalWeight + sortedItems[i].getWeight()
    return '{Value:' + str(totalValue) + ',Cost:' + str(totalWeight) + '}'

def test_knapsack(constraint):
    '''
    Testing the knapsack problem.
    '''
    items = create_menu()
    
    print(knapsack_problem(items , constraint , Food.getValue))
    

test_knapsack(750)