# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 03:47:25 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s sum the triples of even integers!')

#Create a list one through ten
myList = [element for element in range(1,11)]

#Function to use in filter
def even(number):
    """Function to use to determine if a number is even"""
    return number % 2 == 0

#Function to use in map
def multiplyByThree(number):
    """Function to use to multiply a number by 3"""
    return number * 3

#Create a sublist from the original
myList = list(filter(even, myList))

#Multiply the sublist by 3
myList = list(map(multiplyByThree, myList))

#Print the sum of my list
print('This is the sum of the triples of even integers from 2 to 10:', sum(myList))