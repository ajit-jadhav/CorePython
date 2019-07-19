'''
Created on 14-Jul-2019

@author: ajitj
'''
########################## Numpy Multi-dimensional array ################################3
## Program 16 
## create simple array using numpy
from numpy import *
arr = array([10,20,30,40,50]) # create an array
print(arr)#display array


## Program 20 
## create simple array using numpy linspace()
from numpy import *
#divide 0 to 10 into 5 parts and take those points into the array
arr = linspace(0, 10, 5)
print(arr)#display array


##Program 21
## create simple array using numpy logspace()
from numpy import *
#divide the range: 10 power 1 to 10 power 5 into 5 equal parts
arr = logspace(1, 4, 5)
print(arr)#display array


## Program 22 
## create array with even numbers upto 10
from numpy import *
arr = arange(2,11,2) # create an array
print(arr)#display array


## Program 23 
## creating arrays using zeros() and ones()
from numpy import *
a = zeros(5,int)
print(a)#display array
b = ones(5)#default data type is float
print(b)#display array
