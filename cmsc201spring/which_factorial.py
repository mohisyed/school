"""
File:   which_factorial.py
Author:  Mohiuddin Syed
Date:    4/19/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
tells the closest factorial to the given number

"""


def which_factorial(n):
    factorial_list = []
    product = 1
    i = 0
    stop = False
    while not stop:  # n != product
        if n == 0 or n == 1:  # base case
            return 1
        if n >= product:  # if n is greater than the product add it to the product
            product = product * (i + 1)
            i += 1            # goes through the list
            factorial_list.append([i, product])
        if n == product:
            stop = True
        elif n <= product:
            stop = True
    return factorial_list[len(factorial_list) - 1][0]


if __name__ == '__main__':
    user_input = int(input("What is n? "))
    print("the number will be {}".format(which_factorial(user_input)))
