'''
Created on 14-Jul-2019
  
@author: ajitj
'''
  
## Program 11
## to display between m and n
print('to display between m and n')
m,n =[int(i) for i in input("Enter minimum and maximum range:").split(',')]
x = m # Start from m onwards
if x % 2 !=0 : # if x is not even, start from next number
    x = x + 1 
     
while x>=m and x<=n:
    print(x)
    x+=2 
     
print('------------------------------')
  
  
##Program 17
## to display and find the sum of a list of numbers using for loop
print('to display and find the sum of a list of numbers using for loop')
# take a list of numbers
list = [10,20,30,40,50]
sum=0 # initially sum is zero
for i in list:
    print(i) # display element from list 
    sum+=i # add element to sum from list
print('Sum= ', sum)
  
  
## Nested Loops
##Program 19
# To display stars in right angled triangular form
print('To display stars in right angled triangular form')
for i in range(1,11): # to  display 10 raws
    for j in range(1, i+1):# no of stars = row number
        print ('* ',end='')
    print()    
     
          
##Program 20
# To display stars in right angled triangular form - v2
print('To display stars in right angled triangular form')
for i in range(1,11): # to  display 10 raws
    print('* '*(i)) # repeat star for i times         
  
##Program 21
## to display stars in equilateral triangular form
m=1
n=10
for i in range(m,n):
    print(' '*n,end='') # repeat space for n times
    print('* '*(i)) # repeat * for i times
    n-=1
  
## Program 22
# Displaying numbers from 1 to 100 in 10 rows and 10 columns
for x in range(1, 11):
    for y in range(1,11):
        print('{:5}'.format(x*y),end='') # each column size is 8
    print()              
  
## Program 29
# to handle AssertionError raised by assert
x = int(input('Enter a number greater than 0: '))
try:
    assert(x>0) #exception may occur here
    print('U entered: ',x)
except AssertionError:
    print("Wrong input entered") #this is executed in case of
    # exception
      
      
#### Program 32
# program to print prime numbers upto given numbers
# accept upto what number the user wants
max = int(input("upto what number? "))
for num in range(2, max+1): # generate from 2 onwards till max
    for i in range(2,num): # i represents numbers from 2 to num-1
        if(num % i) == 0:    # if number is divisible by i
            break          # then it is not prime, hence go back and check next number        
    else:
        print(num)        
          
####Program 33
#Program to display fibonacci number series
n = int(input('How many fibonaccis ?'))
f1=0 # this is first fibonacci no
f2=1 # this is second fibonacci no
c=2  # count the number of fibonacci
if n==1:
    print(f1)
elif n==2:
    print(f1, '\n', f2, sep='')
else:
    print(f1, '\n', f2, sep='')
    while c<n:
        f = f1+f2 # add two fibonaccis to get the new one
        print(f)
        f1, f2 = f2, f # this is same as f1 = f2, f2=f
        c+=1 #increment counter                        