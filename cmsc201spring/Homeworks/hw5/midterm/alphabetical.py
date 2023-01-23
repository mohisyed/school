"""
File:    alphabetical.py
Author:  Mohiuddin Syed
Date:    3/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
tells if all the characters in the alphabet are in the user input

"""
def alphabetical(a_string):
    order_true = True
    alphabet = "abcdefghijklmnopqrstuvwxyz"  # to compare
    first_letter = []
    second_letter = []
    while order_true:
        for i in range(len(alphabet) - 1):
            if alphabet[i] in a_string and alphabet[i + 1] in a_string:
                first_letter.append(alphabet[i])   # append to compare
                second_letter.append(alphabet[i + 1])
                if first_letter[i] >= second_letter[i]:    # comparing
                    order_true = False 
                    return order_true    # return false
            else:
                order_true = False
                return order_true
        return order_true






if __name__ == '__main__':
    user_input = input("Enter a string to check(or quit): ")
    while user_input != "quit":
        x = alphabetical(user_input)
        if x:
            print("The entire alphabet is in the string in order.")
        else:
            print("The alphabet is not in the string in order.")

        user_input = input("Enter a string to check(or quit): ")

