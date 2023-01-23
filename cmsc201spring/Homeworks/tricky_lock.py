"""
File:   tricky_lock.py
Author:  Mohiuddin Syed
Date: 2/14/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
    User tries to open up a lock. First by entering a number combination
    then by guessing which way to turn the lock.
"""
NUMBER_LOCK_COMBO = 36

first_number = int(input("What is first number in the combination lock? "))
second_number = int(input("What is second number in the combination lock? "))

total_number = first_number + second_number

first_switch = input("what is the position of the first lock? ").lower()
second_switch = input("what is the position of the second lock? ").lower()
third_switch = input("what is the position of the third lock? ").lower()

if first_switch == "up" and second_switch == "up" or third_switch == "up":
        if total_number == NUMBER_LOCK_COMBO:
                    print("Lock opened up")
        else:
                    print("lock clanked")
elif first_switch == "up" or second_switch == "up" and third_switch == "up":
        if total_number == NUMBER_LOCK_COMBO:
                    print("Lock opened up")
        else:
                    print("lock clanked")
else:
        if total_number == NUMBER_LOCK_COMBO:
                    print("Lock clanked")
        else:
                    print("lock didn't budge")
                    
