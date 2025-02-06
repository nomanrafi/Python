# Find the reverse of a number provided by the user (any number of digits).

a = int(input('Enter your number: '))

rev = 0

while a > 0:
    rem = a % 10
    a = a // 10
    rev = (rev * 10) + rem
    
print('Reversed value:', rev)
