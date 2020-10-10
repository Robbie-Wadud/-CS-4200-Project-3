# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:22:17 2020

@author: Robbi
"""

print('Let\'s find the last name "Jones" within a list of tuples')

#Creating the list (firstName, lastName)
names = [('Robbie', 'Wadud'),('Matt', 'Jones'),('Lebron', 'James'),('Sarah', 'Jones'),('Serena', 'Williams'),('Ashley', 'Jones'),('Jessica', 'Jones')]

#Creating the new Jones tuple
jones = tuple(row for row in names if 'Jones' == row[1])

#Spacer
print('')

print(jones)