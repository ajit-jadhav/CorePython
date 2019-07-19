'''
Created on 14-Jul-2019

@author: ajitj
'''

## Program 1
## Creating an integer type array
import array
 
a = array.array('i',[5,6,7])
print('The array elements are: ')
for element in a:
    print (element)
  
      
## Program 2
## Creating an integer type array v2
from array import *
 
a = array('i',[5,6,7])
print('The array elements are: ')
for element in a:
    print (element)
  
  
## Program 3
## Creating an array with group of characters.
from array import *
 
arr = array('u',['a','b','c','d','e'])
print('The array elements are: ')
for ch in arr:
    print (ch)    
          
  
## Program 4
## Creating an array from another array.
from array import *
arr1 = array('d',[1.5,2.5,3,-4])
 
#use same type code and multiply each element of arr1 with 3
arr2 = array(arr1.typecode,(a*3 for a in arr1))
print('The array2 elements are: ')
for i in arr2:
    print (i)    
                  
#################### Indexing and Slicing in Array ###############################
  
## Program 5
## A program to retrieve the elements of an array using rray index
# accessing elements of an array using index
from array import *
x = array('i',[10,20,30,40,50])
 
#find number of elements in array
n=len(x)
#Display array elements using indexing
 
for i in range(n): # repeat from 0 to n-1
    print (x[i],end=' ')                
  
  
## Program 7
## A program that helps to know effects of slicingoperations on an array
from array import *
x = array('i',[10,20,30,40,50])
 
# create array y with elements from 1st to 3rd from x
y = x[1:4]
print(y)
 
# create array y with elements from 0th till end from x
y = x[0:]
print(y)
 
# create array y with elements from 0th to 3rd from x
y = x[0:4]
print(y)
 
# create array y with last 4 elements from x
y = x[-4:]
print(y)
 
# create array y with last 4th element and with 3 [-4-(-1)=-3]elements towards right
y = x[-4:-1]
print(y)
 
# create array y with 0th to 7th elements from x
# Stride 2 means, after 0th element, retrieve every 2nd element from x
y = x[0:7:2]
print(y)



##Program 8:
## Program to retrieve and display only a range of elements from an array using slicing.
# using slicing to display elements of an array
from array import *
x = array('i',[10,20,30,40,50,60,70])
# display elements from 2nd to 4th only
for i in x[2:5]:
    print(i)