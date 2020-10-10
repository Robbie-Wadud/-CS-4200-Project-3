# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:42:29 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s print the index of the max element in a given list of integers!')

#Create list to test
myIntList = [45, 89, 23, 11, -85, 0, 69527, -400, 72, 13245679, -9876543210]

def maxElement(aList):
    """Function to find the max element of a list"""

    #Create a variable for the max element
    maxValue = aList[0]

    #For loop to find the max element
    for element in aList:

        if element > maxValue:
            maxValue = element

    return maxValue

#Creating the maximum value
maximum = maxElement(myIntList)

#Spacer
print('')

#Printing the index of the maximum element
print('This is the index of the max element:', myIntList.index(maximum))