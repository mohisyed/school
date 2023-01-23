"""
File:         hw3_part3.py
Author:       Mohiuddin Syed
Date:         9/26/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Ask the user to input how many steps should the program run. After that the user inputs one of
              of the following commands add, remove, max. depending on what they input the program will either
              add the name, remove the name, or find the name which has the greatest length.
"""
if __name__ == "__main__":
    main_list = []
    user_input = int(input("How many steps should we run? "))

    for i in range(user_input):
        x = input("Enter Command: ")
        x_list_split = x.split()      # creates a split method variable
        if x_list_split[0] == "add":            # if the first word in x is add
            main_list.append(x_list_split[1])          # adds the second word to the list
            print("{} added".format(x_list_split[1]))
        if x_list_split[0] == "remove":
            main_list.remove(x_list_split[1])        # removes the second word from the list
            print("{} remove".format(x_list_split[1]))
        if x_list_split[0] == "max":
            max = main_list[0]                 # creates max variable
            for i in range(len(main_list)):
                if len(main_list[i]) > len(main_list[0]):   # if length of the main list > the length of the first index of the list
                    max = main_list[i]
                elif len(max) == len(main_list[i]):        # if length of max is equal to the current mainlist entry
                    max = main_list[i]
            print("The max name is ", max)

