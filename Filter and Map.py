# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 21:15:10 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s experiment with map and filter calls')

#Rewrite the code
numbers = [10, 3, 7, 1, 9, 4, 2, 8, 5, 6]

#Spacer
print('')

#Original Call
print('This is the original call from the textbook:', list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, numbers))))

#Spacer
print('')

#New Call
print('This is the new call:', list(filter(lambda x: x % 2 == 0, map(lambda x: x * 2, numbers))))

#Spacer
print('')

#Explanation
print('The map function doubles every element in the numbers list. Since every number is multiplied by 2, every number is even, so when the new list goes through the filter function, no elements are removed from the list.')