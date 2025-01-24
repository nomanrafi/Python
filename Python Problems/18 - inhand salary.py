# Write a program that calculates the in-hand salary after deducting HRA (10%), DA (5%), PF (3%), and tax.
# If the salary is between 5-10 lakh, apply a 10% tax;
# for salaries between 11-20 lakh, apply a 20% tax;
# for salaries above 20 lakh, apply a 30% tax.
# If the salary is between 0-1 lakh, print 'k'.

user_input = float(input('Enter your annual salary: '))

if user_input > 500000 and user_input < 1000000:
    tax = (10/100) * user_input
    temp_salary = user_input - tax
elif user_input > 1000000 and user_input < 2000000:
    tax = (20/100) * user_input
    temp_salary = user_input - tax
else:
    tax = (30/100) * user_input
    temp_salary = user_input - tax