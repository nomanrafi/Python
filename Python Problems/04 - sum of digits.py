# Write a program that will give you the sum of three digits.

num = int(input("Enter the three-digit number: "))

a = num % 10  # (123 % 10 = 3)
num = num // 10  # (123 // 10 = 12)