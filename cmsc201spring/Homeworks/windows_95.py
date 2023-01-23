"""
File:    windows_95.py
Author:  Mohiuddin Syed
Date:    2/24/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
   User will input a code and program will check if the code worsk with the windows
   95 rules
"""


enter_key = input("Enter the key: ")
split_key = enter_key.split("-")



if len(split_key[0]) == 3 or len(split_key[1]) == 7:    
    if int(split_key[0]) % 111 != 0:
        x = 0
        for i in range(len(split_key[1])):
            x += int(split_key[1][i])
        if x % 7 == 0:
            print("code is accepted")
        else:
            print("code is not accepted")
    else:
        print("The code is not accepted")
else:
    print("The code is not accepted")
