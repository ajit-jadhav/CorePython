'''
Created on 11-Jul-2019

@author: ajitj
'''

#Create a list of byte array numbers
elements = [10, 20, 0, 40, 15]

#Convert list into bytearray type array
x = bytearray(elements)

#Modify the first two elements
x[0] = 88
x[1] = 99

#Retrieve elements from x using for loop and display
for i in x: print(i)
