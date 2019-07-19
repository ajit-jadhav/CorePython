'''
Created on 14-Jul-2019

@author: ajitj
'''
################## Mathematical operations on array  #########################

## Program 24
# Creating numpy array
from numpy import *
arr = array([10,20,30.5,-40])
print('Original array:',arr)

#Perform arithmetic operations on an array
print('After adding 5: ',arr+5)
print('After subtracting 5: ',arr-5)
print('After multiplying with 5: ',arr*5)
print('After dividing with 5: ',arr/5)
print('After modulus with 5: ',arr%5)

#we can use arrays in expression also
print('Expression value: ',(arr+5)**2-10)

#do some math functions
print('sin values: ',sin(arr))
print('cos values: ',cos(arr))
print('tan values: ',tan(arr))
print('Biggest element: ',max(arr))
print('smallest element: ',min(arr))
print('sum of all elements: ',sum(arr))
print('average of all elements: ',mean(arr))



