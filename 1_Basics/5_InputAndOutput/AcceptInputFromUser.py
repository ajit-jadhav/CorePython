'''
Created on 11-Jul-2019

@author: ajitj
'''

##Program-1
## Accepting String from keyboard
print('Accepting String from keyboard')
str = input("Enter a string: ")
print('U entered: ',str)# Display entire string

print('-------------------------------')


##Program-2
## Accepting String or a character from keyboard
print('Accepting String or a character from keyboard')
ch = input("Enter a character: ")
print('U entered: ',ch)

print('-------------------------------')


##Program-3
## Accepting single character from keyboard
print('Accepting single character from keyboard')
ch = input("Enter a char: ")
print('U entered: '+ch[0])

print('-------------------------------')


##Program-4
## Accepting integer from keyboard
print('Accepting integer from keyboard')
str = input("Enter a Number: ")
x= int(str)
print('U entered: ', x)

print('-------------------------------')


##Program-5
## Accepting integer from keyboard - V2 
print('Accepting integer from keyboard - V2')
x= int(input("Enter a Number: "))
print('U entered: ', x)

print('-------------------------------')


##Program-6
## Accepting float from keyboard
print('Accepting float from keyboard') 
x= float(input("Enter a Number: "))
print('U entered: ', x)

print('-------------------------------')


##Program-7
## Accepting two integer numbers from keyboard
print('Accepting two integer numbers from keyboard') 
x = int(input("Enter first Number: "))
y = int(input("Enter second Number: "))
print('U entered: ', x, y) ## Displaying both numbers separating with space
print('-------------------------------')


##Program-8
## Finding sum of two numbers.
print('Finding sum of two numbers.') 
x = int(input("Enter first Number: "))
y = int(input("Enter second Number: "))
print('The sum of ',x, ' and ', y, 'is', x+y) ## Displaying sum
print('The sum of {} and {} is {}'.format(x, y, x+y)) ## Displaying again

print('-------------------------------')


##Program-9
## Finding sum and product of two numbers.
print('Finding sum of two numbers.') 
x = int(input("Enter first Number: "))
y = int(input("Enter second Number: "))
print('The sum of ',x, ' and ', y, 'is', x+y) ## Displaying sum
print('The sum of {} and {} is {}'.format(x, y, x+y)) ## Displaying again

print('-------------------------------')


##Program-10
## Input from other number system
print('Input from other number system.') 
str = input("Enter hexadecimal Number: ") #Accept input as string
n = int(str, 16) # inform the number is base 16
print("Hexadecimal to decimal= ", n)

str = input("Enter octal Number: ") #Accept input as string
n = int(str, 8) # inform the number is base 8
print("octal to decimal= ", n)

str = input("Enter binary Number: ") #Accept input as string
n = int(str, 2) # inform the number is base 2
print("binary to decimal= ", n)

print('-------------------------------')


##Program-11
## Accepting three numbers separated by space
print('Accepting three numbers separated by space')
var1, var2,var3 = [int(x) for x in input("Enter three numbers: ").split()]
print("Sum = ",var1+var2+var3)

print('-------------------------------')


##Program-12
##Accepting three numbers separated by comma
print('Accepting three numbers separated by comma')
var1, var2,var3 = [int(x) for x in input("Enter three numbers: ").split(',')]
print("Sum = ",var1+var2+var3)

print('-------------------------------')


##Program-13
##Accepting group of string from keyboard
print('Accepting group of string from keyboard')
list = [x for x in input("Enter strings: ").split(',')]
print("You Entered:\n",list)

print('-------------------------------')


##Program-14
## Using eval() along with input() function
print("Using eval() along with input() function")
x = eval(input("Enter an expression: "))
print("Result= %d" % x)

print('-------------------------------')


##Program-15
## accepting list from keyword and eval
print("accepting list from keyword and eval")
lst = eval(input("Enter a List: "))
print("List= " % lst)


print('-------------------------------')

##Program-16
## accepting tuple from keyword and eval
print("accepting tuple from keyword and eval")
tpl = eval(input("Enter a tuple: "))
print("tuple= " % tpl)

print('-------------------------------')