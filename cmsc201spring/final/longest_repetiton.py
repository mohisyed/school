"""
File:   which_factorial.py
Author:  Mohiuddin Syed
Date:    4/19/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
tells the closest factorial to the given number

"""


def longest_repetition(a_string):
    counter = 0
    counter_2 = []
    for i in range(len(a_string) - 1):
        if a_string[i] == a_string[i + 1]:  # if its the same add it to the counter
            counter += 1
        elif a_string[i] != a_string[i + 1]:   # if not equal to add it to the counter but also append it to the second list
            counter += 1
            counter_2.append(counter)
            counter = 0   # reset the counter basically just keeping track of the list

    x = 0
    for i in range(len(counter_2)):
        if x < counter_2[i]:          # if its less than 0 x = 0
            x = counter_2[i]
    return print(x)


if __name__ == '__main__':
    longest_repetition('aaabbc')
    longest_repetition('abcdkjfasdlkfnafnbbbcedflsj')
    longest_repetition("aaabbccccccddeeeeee")
