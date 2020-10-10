# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:03:56 2020

@author: Robbie
"""

#Introduce the program
print('Let\'s sort and remove duplicates from a list!')

#Creating lists to use for testing later
listOne = [45, -60, 23, 9, 0, -84, -84, 45, -84]
listTwo = ['I am', 'Doing', 'Some', 'Things', 'Victorious', 'chicken', 'zebra', 'good', 'zebra', 'awesome', 'zebra', 'good', 'zebra']
listThree = [-5.6, 8.7, 10.2, 2.1, -56.49, 2020.2021, 2.1]

#Function to sort a list and remove duplicates from a list
def sortAndRemoveDuplicates(aList):
    """This function sorts and removes duplicates from a list"""

    #Sort the list
    aList = sorted(aList)

    #Creating the final list
    finalList = []

    #For loop to iterate through the list to remove duplicate elements
    for element in aList:

        if element not in finalList:
            finalList.append(element)

    return finalList

#Spacer
print('')

#Testing the function with different types of lists
print('My function with integers:', sortAndRemoveDuplicates(listOne))

#Spacer
print('')

#Testing the function with different types of lists
print('My function with strings:', sortAndRemoveDuplicates(listTwo))

#Spacer
print('')

#Testing the function with different types of lists
print('My function with floating-point numbers:', sortAndRemoveDuplicates(listThree))