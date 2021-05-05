# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 15:40:46 2021

@author: Arijit
"""

class Person:
    
    def __init__(self , name , height , weight , bmi = 0 , bmi_status = ""):
        
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = bmi
        self.bmi_status = bmi_status
        
        
    def calculateBmi(self):
        self.bmi = round(self.weight / (self.height * self.height))
        

class Society:
    
    def __init__(self , bmi_status , person_list):
        self.persons = person_list
        
        self.s_bmi_status = bmi_status
        for bmi_stat in bmi_status:
            if bmi_status[bmi_stat][0] > bmi_status[bmi_stat][1]:
                bmi_status[bmi_stat] = (bmi_status[bmi_stat][1] , bmi_status[bmi_stat][0])
        
    def calculateBmiAndStatusByName(self , name):
        
        for each_person in self.persons:
            idx = self.persons.index(each_person)
            if each_person.name.lower() == name.lower():
                each_person.calculateBmi()
                each_person.bmi_status = list(self.s_bmi_status.keys())[idx]
                return True
                
        else:
            return False
        
    def removeInvalidPersons(self , bmi_val):
        
        invalid_person = []
        for each_person in self.persons:
            
            if each_person.bmi < bmi_val:
                invalid_person.append(each_person)
                
        return invalid_person
    
    
if __name__  == '__main__':
    num_persons = int(input('Enter number of persons?'))
    
    person_list = []
    
    for i in range(num_persons):
        person_name = input('Enter name')
        weight = int(input('Enter height?'))
        height = int(input('Enter weight?'))
        person_list.append(Person(person_name.lower() , height , weight))
    
    num_val = int(input('How many elements are to be there?'))
    
    bmi_stat_dict = {}
    
    for i in range(num_val):
        status_of_bmi = input('Enter BMI status?')
    
        low = int(input('Enter lower bmi'))
    
        high = int(input('Enter higher bmi'))
        
        bmi_stat_dict[status_of_bmi] = (low , high)
                
    
    
    society = Society(bmi_stat_dict , person_list)
    
    check_name = input('Enter Name')
    check_bmi = int(input('Enter a number'))
    
    if society.calculateBmiAndStatusByName(check_name):
        for p in person_list:
            if (p.name.lower() == check_name) and (p.bmi != 0):
                print(p.bmi)
                print(p.bmi_status)
    else:
        print('No Person Exists')
    
    invalid_lst = society.removeInvalidPersons(check_bmi)
    
    for lst_elem in invalid_lst:
        print(lst_elem.name)
        print(lst_elem.bmi)
    
        