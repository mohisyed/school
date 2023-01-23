"""
File:    perfection.py
Author:  Mohiuddin Syed
Date:    3/9/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    calcualtes the perfect sum of a number if its possible
"""
user_input = int(input("What number do you want to input? "))

perfect_divisors = []
total = 0
last_string = ""
if user_input == 1:
    print("This is not a perfect number")
elif user_input != 1:
    for i in range(user_input):
        if i != 0:
            x = user_input % i
            if x == 0:
                perfect_divisors.append(i)

for i in range(len(perfect_divisors)):
    total += perfect_divisors[i]
    if len(perfect_divisors) - 1 == i:
        last_string += " {} ".format(perfect_divisors[i])
    else:
        last_string += " {} +".format(perfect_divisors[i])
if total == user_input:
    print("This is a perfect number: {}".format(total))
    print(last_string + "= {}".format(total))
elif total != user_input:
    print("this isn't a perfect string")
    print(last_string + "= {}".format(total))
