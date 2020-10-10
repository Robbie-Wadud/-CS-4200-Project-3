# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:31:03 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s perform slice operations!')

#Creating the var
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Printing out part a
print('\nThis is the first half of the alphabet using the starting and ending indices:', alphabet[0:14])

#Printing out part b
print('\nThis is the first half of the alphabet using only the ending index:', alphabet[:14])

#Printing out part c
print('\nThis is the second half of the alphabet using the starting and ending indices:', alphabet[14:len(alphabet)])

#Printing out part d
print('\nThis is the second half of the alphabet using only the starting index:', alphabet[14:])

#Printing out part e
print('\nThis is every second letter in the alphabet:', alphabet[::2])

#Printing out part f
print('\nThis is the alphabet in reverse:', alphabet[::-1])

#Printing out part g
print('\nThis is the alphabet in reverse AND only every third letter:', alphabet[::-3])