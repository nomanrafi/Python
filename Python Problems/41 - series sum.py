# Write a program to find the sum of the series up to the nth term:

# 1 + x^2/2 + x^3/3 + ... + x^n/n

# The value of n will be provided by the user.

x = int(input('Enter your number: '))
n = int(input('Enter nth value: '))

sum = 1

for i in range(2, n + 1):
    sum = sum + ((x**i)/i)
    