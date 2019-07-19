'''
Created on 14-Jul-2019

@author: ajitj
'''
## Program 35
## retrieving the elements from a 2D array using indexing 
from numpy import *
# create a 2D array with 3 rows and 3 cols
a = [[1,2,3],[4,5,6],[7,8,9]]
# display only rows
for i in range(len(a)):
    print(a[i])
#display element by element
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j],end=' ')   
 
           
## Program 36
## retrieving the elements from a 3D array using indexing 
from numpy import *
# create a 3D array with size 2x2x3
a = [[[1,2,3],
      [4,5,6]],
        
     [[7,8,9],
      [10,11,12]]]
# display element by element
for i in range(len(a)):
    for j in range(len(a[i])):
        for k in range(len(a[i][j])):
            print(a[i][j][k],end=' ')   
        print()        
    print()    
 
 
## Program 37
## Program to accept matrix from user and display it's transpose matrix
from numpy import *
# accept number of rows and columns into r and c
r, c = [int(a) for a in input("Enter number of row and column").split()]
#accept matrix elements as a string into str
str = input('Enter matrix elements:\n ')
#Convert the string into a matrix with size rxc
x = reshape(matrix(str), (r,c))
print('The original matrix: ')
print(x)
  
print('The transpose matrix: ')
y = x.transpose()
print(y)


# Program 38
# Program to accept two matrices and find their product
import sys
from numpy import *
# accept number of rows and columns of first matrix into r1,c1
r1, c1 = [int(a) for a in input("Enter first matrix number of row and column").split()]
# accept number of rows and columns of second matrix into r2,c2
r2, c2 = [int(a) for a in input("Enter second matrix number of row and column").split()]
#test the condition if multiplication is possible
if c1!=r2:
    print('Multiplication not possible')
    sys.exit()   
#accept first matrix elements as a string into str1
str1 = input('Enter first matrix elements:\n ')
#accept second matrix elements as a string into str2
str2 = input('Enter second matrix elements:\n ')

#Convert the str1 string into a matrix with size r1xc1
x = reshape(matrix(str1), (r1,c1))

#Convert the str2 string into a matrix with size r2xc2
y = reshape(matrix(str2), (r2,c2))

print('the product matrix: ')
z=x*y
print(z)