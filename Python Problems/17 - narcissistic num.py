# Write a program that will take user input of a (4-digit number) and check whether the number is a narcissist number or not.

user_input = int(input("Enter a four digit number: "))

num = user_input

a = num % 10
num = num // 10
b = num % 10
num = num // 10
c = num % 10
d = num // 10
