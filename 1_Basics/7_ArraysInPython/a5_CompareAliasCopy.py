'''
Created on 14-Jul-2019

@author: ajitj
'''
###################### Comparing Arrays ##########################

## Program 25
#Program to compare two arrays and return resultant boolean type array
from numpy import *
a = array([1,2,3,0])
b = array([0,2,3,1])
c = a==b 
print('Result of a==b',c)
c = a>b 
print('Result of a>b',c)
c = a<=b 
print('Result of a<=b',c)
 
 
######Using all() and any() functions########
## Program 26
from numpy import *
a = array([1,2,3,0])
b = array([0,2,3,1])
c = a>b
print('result of a>b: ',c)
 
print('Check if any one element is true: ',any(c))
print('Check if all elements are true: ',all(c))
 
if(any(a>b)):
    print('a contains at least one element greater than those of b')
 
 
## Program 27
## Demonstrate logical and or and not
from numpy import *
a = array([1,2,3], int)
b = array([0,2,3], int)
c = logical_and(a>0, a<4)
print('logical_and',c)
 
c = logical_or(b>=0, b==1)
print('logical_or',c)
 
c = logical_not(b)
print('logical_not',c)
 
 
## Program 28
## compare corresponding elements in array and retrieve biggest element using where() function
from numpy import *
a = array([10,20,30,40,50], int)
b = array([1,21,3,40,51], int)
# if a>b then take element from a else from b
c = where(a>b,a,b)
print('Array formed by where() function:\n ',c)


## Program 29
## Getting nonzero elements from array using nonzero() function
from numpy import *
a = array([1,2,0,-1,0,6], int)
#Retrive indexes of nonzero elements
c = nonzero(a)
#display indexes
for i in c: 
    print(i)
print('Array formed by nonzero() function:')
#display nonzero elements
print(a[c])


## Program 30
## Alias an array and understand the affect of aliasing
from numpy import *
a = arange(1,6) #create a with elements 1 to 5
b = a #give another name b to a
print('Original array: ',a)
print('Alias array: ',b) 
 
b[0]=99 #Modify 0th element of b
print('After modification: ')
print('Original array: ',a)
print('Alias array: ',b)
 
 
## Program 31
## Creating a view for an array
from numpy import *
a = arange(1,6) #create a with elements 1 to 5
b = a.view() #create a view of a and call it b
print('Original array: ',a)
print('New array: ',b) 
 
b[0]=99 #Modify 0th element of b
print('After modification: ')
print('Original array: ',a)
print('New array: ',b)
 
 
## Program 32
## Copying an array
from numpy import *
a = arange(1,6) #create a with elements 1 to 5
b = a.copy() #create a copy of a and call it b
print('Original array: ',a)
print('New array: ',b) 
 
b[0]=99 #Modify 0th element of b
print('After modification: ')
print('Original array: ',a)
print('New array: ',b)
 
 
## Program 33 
## Slicing operations on arrays
from numpy import *
a = arange(10,16) #create a with elements 10 to 15
print(a)
#retrieve from 1st to one element prior to 6th element in steps of 2
b = a[1:6:2]
print(b)
#retrieve all elements from a
b = a[::]
print(b)
#retrieve from 6-2= 4th to one element prior to 2nd element in
#decreasing step size
b = a[-2:2:-1]
print(b)
#retrieve from 0th to one element prior to 4th element (6-2=4th)
b = a[:-2:]
print(b)


## Program 34 
## displaying elements of numpy array using indexing
from numpy import *
a = arange(10,16) #create a with elements 10 to 15
print(a)
#retrieve from 1st to one element prior to 6th element in steps of 2
b = a[1:6:2]
print(b)
#display elements using indexing
i=0
while(i<len(a)):
    print(a[i])
    i+=1