"""
Write a program that will take hours and rate per hour as input and will compute the total payment.
 your program will give the employee 1.5 times the hourly rate for hours worked above 40 hours.

Here your program will show an error message for non-numeric value of hours/rate.
 After showing the error message, the program will exit

Example 01:
Enter Hours: 45
Enter Rate: 10
Pay: 475.00


Example 02:
Enter Hours: 45
Enter Rate: nine
Error, please enter numeric input

"""


# your code here

try:
# take hours and rate as input
    hours = int(input('Enter Hours: '))

    rate = float(input('Enter Rate:'))
except ValueError:
    print("Error, please enter numeric input")

pay = 0


print('Pay: {:.2f}'.format(pay))
