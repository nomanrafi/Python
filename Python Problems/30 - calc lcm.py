# The user will provide two numbers, and you have to find the LCM of those two numbers.

a = int(input('Enter your first number: '))
num_1 = a
b = int(input('Enter your second number: '))
num_2 = b
while num_1 % num_2 != 0:
    rem = num_1 % num_2
    num_1 = num_2
    num_2 = rem
    