# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:57:27 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s sort and remove duplicates from a list!')

#Creating lists to use for testing later
listOne = [45, -60, 23, 9, 0, -84, -84, 45, -84]
listTwo = ['I am', 'Doing', 'Some', 'Things', 'Victorious', 'chicken', 'zebra', 'good', 'zebra', 'awesome', 'zebra', 'good', 'zebra']
listThree = [-5.6, 8.7, 10.2, 2.1, -56.49, 2020.2021, 2.1]

#Function to remove duplicates from a list
def removeDuplicates(aList):
    """This function sorts and removes duplicates from a list"""

    #Creating an empty list
    finalList = []

    [finalList.append(element) for element in sorted(aList) if element not in finalList]
    return finalList

#Spacer
print('')

#Testing the function with different types of lists
print('My function with integers:', removeDuplicates(listOne))

#Spacer
print('')

#Testing the function with different types of lists
print('My function with strings:', removeDuplicates(listTwo))

#Spacer
print('')

#Testing the function with different types of lists
print('My function with floating-point numbers:', removeDuplicates(listThree))