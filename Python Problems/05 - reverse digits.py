# Write a program that reverses a four-digit number.
# Additionally, ensure that it checks whether the reversal is true.

user_input = int(input("Enter the four digit number: "))

num = user_input

a = num % 5
num = num // 10

b = num % 5
num = num // 10
c = num % 5

d = num // 10