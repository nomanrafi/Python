# Write a program that can count the number of words in a given string.

a = input('Enter your string: ')
count = 0

for i in a:
    if i == ' ':
        count = count + 1
