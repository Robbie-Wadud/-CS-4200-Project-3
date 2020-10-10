# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 03:36:37 2020

NOT DONE YET NOT DONE YET NOT DONE YET
NOT DONE YET NOT DONE YET NOT DONE YET
NOT DONE YET NOT DONE YET NOT DONE YET
NOT DONE YET NOT DONE YET NOT DONE YET

@author: Robbi
"""

#Introduce the program
print('Let\'s sort and remove duplicates from a list AND have the element\'s count!')

#Creating lists to use for testing later
listOne = [45, -60, 23, 9, 0, -84, -84, 45, -84]
listTwo = ['I am', 'Doing', 'Some', 'Things', 'Victorious', 'chicken', 'zebra', 'good', 'zebra', 'awesome', 'zebra', 'good', 'zebra']
listThree = [-5.6, 8.7, 10.2, 2.1, -56.49, 2020.2021, 2.1]

#Creating an empty list
#finalList = []

#Function to remove duplicates from a list and output their count
def removeDuplicatesAndStoringCounts(aList):
    """This function sorts and removes duplicates from a list AND collects their counts"""

    #Creating an empty list
    finalList = []

    [finalList.append(element) for element in sorted(aList) if element not in finalList]
    return finalList

#Spacer
print('')

#Testing the function with different types of lists
print('My function with integers:', removeDuplicatesAndStoringCounts(listOne))

#Spacer
print('')

#Testing the function with different types of lists
print('My function with strings:', removeDuplicatesAndStoringCounts(listTwo))

#Spacer
print('')

#Testing the function with different types of lists
print('My function with floating-point numbers:', removeDuplicatesAndStoringCounts(listThree))