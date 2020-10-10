# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 19:28:54 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s find the last name "Jones" within a list of tuples')

#Creating the list (firstName, lastName)
names = [('Robbie', 'Wadud'),('Matt', 'Jones'),('Lebron', 'James'),('Sarah', 'Jones'),('Serena', 'Williams'),('Ashley', 'Jones'),('Jessica', 'Jones')]

#Function to find the last name Jones
def findJones(aList):
    """This function finds the last name Jones in a list of tuples"""
    return aList[1] == 'Jones'

#Creating the list of jones
jones = tuple(filter(findJones, names))

#Spacer
print('')

print(jones)