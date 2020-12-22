# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 13:36:25 2020

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
    
    def getCost(self): #getter for weight
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

#Lets create our search tree
def search_tree(items , maxConstraint):
    
    avail = maxConstraint
    
    if (len(items) == 0) or (avail <= 0): #checking if there is some availability of data
        return 0 
       
    elif items[0].getCost() > avail: #checking if we can only follow the right path
            result = search_tree(items[1:] , avail)
    
    else: #taking the left path
        nextItem = items[0]
        
        #calculating the left path value
        withVal = search_tree(items[1:] , avail - nextItem.getCost())
        withVal += nextItem.getValue()
        #calculating the right path value
        withoutVal = search_tree(items[1:] , avail)
        
        #checking if we need the left or the right path
        if withVal > withoutVal:
            result = withVal
        else:
            result = withoutVal
    
    return result