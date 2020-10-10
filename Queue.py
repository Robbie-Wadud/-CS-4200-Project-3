# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 20:57:16 2020

@author: Robbi
"""

#Introduce the program
print('Let\'s simulate a queue')

#Creating the queue
queue = []

#Spacer
print('')

print('This is our empty queue:', queue)

#Enqueue 3
queue.append(3)

#Spacer
print('')

#Printing the queue
print('This is the queue after one enqueue:', queue)

#Enqueue 2
queue.append(2)

#Spacer
print('')

#Printing the queue
print('This is the queue after two enqueues:', queue)

#Enqueue 1
queue.append(1)

#Spacer
print('')

#Printing the queue
print('This is the queue after three enqueues:', queue)

#Dequeue 3
queue.pop(0)

#Spacer
print('')

#Printing the queue
print('This is the queue after one dequeue:', queue)

#Dequeue 2
queue.pop(0)

#Spacer
print('')

#Printing the queue
print('This is the queue after two dequeues:', queue)

#Dequeue 1
queue.pop(0)

#Spacer
print('')

#Printing the queue
print('This is the queue after three dequeues:', queue)