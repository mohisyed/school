"""
File:    ascending.py
Author:  Mohiuddin Syed
Date:    2/24/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
program will check if the next letter is larger than the previous one. 
will print whether or not the function will "ascend"

"""

original_string = input("enter your test string: ").lower()
ASCENDING = "string is ascending"
NOT_ASCENDING = "string is not ascending"
x = True
i = 1
ascending_not = []
while x:
    if original_string[i - 1] >= original_string[i]:
        ascending_not.append(NOT_ASCENDING)
        x = False

    elif original_string[i - 1] < original_string[i]:
        ascending_not.append(ASCENDING)
        if i < len(original_string) - 1:
            i += 1
        else:
            x = False

if not x:
    print(ascending_not[i-1])
