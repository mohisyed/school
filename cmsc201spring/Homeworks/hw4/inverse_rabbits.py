"""
File:    inverse_rabbits.py
Author:  Mohiuddin Syed
Date:    2/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    Program uses the Fibonacci sequence to calculate how many months it takes
      
"""

user_input = int(input("How many rabbits do you want? "))

n2_rabbit = 0
n1_rabbit = 2
total_rabbits = 0
months = 0

while total_rabbits < user_input:
    if months == 0:
        total_rabbits = n1_rabbit
        print("in month {} we have {} rabbits".format(months, total_rabbits))
        months = 1
    elif months == 1:
        total_rabbits = n1_rabbit + n2_rabbit
        print("in month {} we have {} rabbits".format(months, total_rabbits))
        months = 2
    elif months >= 2:
        n2_rabbit = n1_rabbit
        n1_rabbit = total_rabbits
        total_rabbits = n1_rabbit + n2_rabbit
        print("in month {} we have {} rabbits".format(months, total_rabbits))
        months += 1
    
print("It will take {} to have {} rabbits".format(months - 1, user_input))
