"""
File:         square_freeness.py
Author:       Mohiuddin Syed
Date:         10/7/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Finds the natrual numbers that are square free
"""

if __name__ == "__main__":

    user_x_input = int(input("Tell me a number x "))
    checker = 2
    counter = 0
    finalx = 0

    if user_x_input <= 0:    # less than 0 ,invalid
        print("invalid")

    if checker < user_x_input:
        if user_x_input % checker == 0: # modulo operator gives remandier of userx/ checker
            while user_x_input % checker == 0:  # if remainder = 0
                finalx = user_x_input / checker  # reassign the variable
                counter += 1
            if counter >= 2:      # cond of not square free numb
                print("{} is not square free {} squared divides it".format(user_x_input, checker))
        checker += 1
    else:
        print(user_x_input, "is square free")
