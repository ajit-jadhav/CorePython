'''
Created on 14-Jul-2019

@author: ajitj
'''
## Program 9
## Program to understand various methods of arrays class
 
#Operations on arrays
from array import *
 
#Create an array int values
arr = array('i',[10,20,30,40,50])
print('Original array: ',arr)
 
#append 30 to the array arr
arr.append(30)
arr.append(60)
print('After appending 30,60 to an array: ',arr)
 
#insert 99 at position number 1 to arr
arr.insert(1,99)
print('After inserting 99 to 1st position: ',arr)
 
#remove an element from an array
arr.remove(20)
print('After removing 20 from an array: ',arr)
 
 
#insert 99 at position number 1 to arr
arr.insert(1,99)
print('After inserting 99 to 1st position: ',arr)
 
#remove an element from an array using pop() method
n = arr.pop()
print('Array after using pop():',arr)
print('popped element: ',n)
 
#finding position of element using index() method
n = arr.index(30)
print('first occurrence of element 30 is at',n)
 
 
# Convert an arry items to list using tolist() method
lst = arr.tolist()
print('List: ' ,lst)
print('Array: ',arr)



##Program 10
## Storing students marks in an array and finding total marks and percentage.
 
from array import *
# accept marks as string
str = input('Enter marks: ').split(',')
#Store marks into 'marks' array
marks = [int(num) for num in str]
#display marks and find total
sum=0
for x in marks:
    print(x)
    sum+=x
print('Total marks: ',sum)
#display percentage
n = len(marks)
percent = sum/n
print('Percentage: ',percent)


####Program 11
## Sort Array element using bubble sort technique
from array import *
#create an empty array to store integers
x = array('i',[])
#store elements into the array x
print('how many elements? ',end='')
n = int(input())#accept input into n
for i in range(n): # repeat for n times
    print('Enter element: ',end='')
    x.append(int(input())) # add element to the array x
print('Original array: ',x)
#bubble sort
flag = False #when swapping is done, flag becomes true
for i in range(n-1):# i is from 0 to n-1
    for j in range (n-1-i): # j is from 0 to one element lesser than i
        if x[j]>x[j+1]: # if first element is bigger than the 2nd one
            t = x[j] #swap j and j+1 elements
            x[j] = x[j+1]
            x[j+1] = t
            flag = True # swapping done, hence flag id true
    if flag==False: # no swapping means array is in sorted order
        break # come out of inner for loop
    else:
        flag = False # assign initial value to flag
print('Sorted array= ',x)


####Program 12
# Search for the position of an element in an array using sequential search
from array import *
#create an empty array to store integers
x = array('i',[])
#store elements into the array x
print('how many elements? ',end='')
n = int(input())#accept input into n
for i in range(n): # repeat for n times
    print('Enter element: ',end='')
    x.append(int(input())) # add element to the array x
print('Original array: ',x)
s = int(input('Enter string to search:'))
##Linear search or sequential search
flag = False # this becomes True if element is found
for i in range(len(x)):
    if s==x[i]:
        print('Found at position =',i+1)
        flag=True
if flag==False:
    print('Not found in the array')        



## Program 13:
## Program to search for the position of an element in an array using index() method
from array import *
#create an empty array to store integers
x = array('i',[])
#store elements into the array x
print('how many elements? ',end='')
n = int(input())#accept input into n
for i in range(n): # repeat for n times
    print('Enter element: ',end='')
    x.append(int(input())) # add element to the array x
print('Original array: ',x)
s = int(input('Enter string to search:'))
#index() method gives location of the element in the array
try:
    pos = x.index(s)
    print('Found at position: ',pos+1)
except ValueError: # if element not found then Value Error will raise
    print('Not found in the array')
    