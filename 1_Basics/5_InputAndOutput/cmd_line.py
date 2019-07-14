'''
Created on 12-Jul-2019

@author: ajitj
'''
## Program - 17
## To display command line args.
import sys
n = len(sys.argv) #n is the number of arguments
args = sys.argv #args list contains arguments
print('No. of command line args: ',n)
print('The args are: ',args)
print('The args one by one: ')
for a in args:
    print(a)
    
print('-------------------------------------------')


## Program - 18
## Add two numbers.
import sys
##Convert args into integers and add them
sum = int(sys.argv[1])+int(sys.argv[2])
print('Sum= ', sum)
    
print('-------------------------------------------')


## Program - 19
## to find sum of even numbers
import sys
# read command line args except the program name
args = sys.argv[1:]
print(args)
sum = 0
#Find sum of even arguments
for a in args:
    x = int(a)
    if x%2==0:
        sum+=x
print('Sum of even numbers: ',sum)
        
print('-------------------------------------------')


## Program - 20
## To find square of a given number.
import argparse

#Create ArgumentPArser class object
parser = argparse.ArgumentParser(description='This program displays square value of given number')    
#Add one argument as name num and type as integer
parser.add_argument("num",type=int,help='Please input integer type number.')
#Retrieve the arguments passed to the program
args = parser.parse_args()
#Find square of argument passed
result = args.num**2
print('Square value: ', result)

print('-------------------------------------------')


## Program - 21
## To find sum of two given numbers
import argparse
#Create ArgumentPArser class object
parser = argparse.ArgumentParser(description='This program calculates sum of two given numbers')    
#Add two arguments as name n1 and n2 and type as float
parser.add_argument("n1",type=float,help='Please input float type number.')
parser.add_argument("n2",type=float,help='Please input float type number.')
#Retrieve the arguments passed to the program
args = parser.parse_args()
#Find square of argument passed
result = float(args.n1) + float(args.n2)
print('Sum of two: ', result)

    
print('-------------------------------------------')


## Program - 22
## A Python program to find power value of a number when it is raised to perticular power.
#To find power value of a number.
import argparse
#call ArgumentParser
parser = argparse.ArgumentParser()    
#Add two arguments to ther parser
parser.add_argument("nums",nargs=2)
#Retrieve the arguments into args object
args = parser.parse_args()
#Find the power value
#args.nums represents a list
print('Its power= ',args.num[1])
#Convert argument into float and then find power
result = float(args.nums[0])**float(args.nums[2])
print('Result= ', result)

print('-------------------------------------------')


## Program - 23
## A Python program to accept one more argument and display them as list elements.
import argparse
#call ArgumentParser
parser = argparse.ArgumentParser()    
#Add two arguments to parser
parser.add_argument("nums",nargs='+')
#Retrieve the arguments into args object
args = parser.parse_args()
for x in args.nums:
    print(x)
    
print('-------------------------------------------')