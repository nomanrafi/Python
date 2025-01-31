# Write a menu-driven program with the following options:

# 1. cm to inch,
# 2. km to miles,
# 3. USD to INR,
# 4. exit.

user_input = input('''
Hi! Welcome to my page
What would you like to do?
1. Convert cm to inches
2. Convert km to miles
3. Convert usd to inr
4. Exit''')
if user_input == '1':
    cm = float(input('Enter value in cm: '))
    inch = cm * 0.394
    print('Your value in inches is:', inch)