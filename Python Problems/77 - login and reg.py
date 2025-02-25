# Write a dummy program that can perform login and registration using a menu-driven approach.

database = {}

def user_menu():
    user_input = input('''
    1. Enter 1 to Register
    2. Enter 2 to Login
    3. Enter 3 to Exit
    ''')
    
    if user_input == '1':
        register()
    elif user_input == '2':
        login()
    else:
        print('Bye')
