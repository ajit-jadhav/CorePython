'''
Created on 10-Jul-2019

@author: ajitj
'''
# 3. Program to convert convert octal, binary, hexadecimal numbers to decimal
n1 = 0o17
n2 = 0B1110010
n3 = 0X1c2

n = int(n1)
print('Octal 17 = ', n)
n = int(n2)
print('Binary 1110010 = ', n)
n = int(n3)
print('Hexadecimal 1c2 = ', n)

print('------------------------------------------')

# 4. Program to convert into decimal number from strings

s1 = "17"
s2 = "1110010"
s3 = "1c2"

n = int(s1,8)
print('Octal 17 = ', n)
n = int(s2,2)
print('Binary 1110010 = ', n)
n = int(s3,16)
print('Hexadecimal 1c2 = ', n)
