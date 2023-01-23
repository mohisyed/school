"""
File:   roller_coaster.py
Author:  Mohiuddin Syed
Date:    4/19/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
calculates the total amount of fun on the roller coaster
"""




def roller_coaster(height_list):

    current_height = 0   # calculates total height
    current_height_list = []   # has all the current height lists
    for i in range(len(height_list) - 1):
        if i == 0:
            if height_list[i] > height_list[i + 1]:  # if index 0 is greater than 1
                current_height += height_list[i] - height_list[i + 1]   # subtract the 2 to get the current height
            elif height_list[i] <= height_list[i + 1]:         # elif less than then append the current and make it to 0
                current_height_list.append(current_height)
                current_height = 0
        elif i >= 1:
            if height_list[i] > height_list[i + 1]:
                current_height += height_list[i] - height_list[i + 1]
            elif height_list[i] <= height_list[i + 1]:
                current_height_list.append(current_height)
                current_height = 0
        elif i == len(height_list) - 1:
            if height_list[i] <= height_list[i - 1]:
                current_height_list.append(current_height)
                current_height = 0
            elif height_list[i] >= height_list[i - 1]:
                current_height += height_list[i] - height_list[i + 1]

    print(current_height_list)
    total_fun = 0
    for i in range(len(current_height_list)):    # calulates the total fun
        total_fun += (current_height_list[i] * 2 * 9.8) ** (1/2)
    print(total_fun)



if __name__ == '__main__':
    height_list = [0, 1, 5, 2, 0, 5, 4, 3, 2, 1, 2, 3, 4, 5, 3, 0, 5]
    second_height_list = [0, 100, 50, 0, 10]
    print(roller_coaster(height_list))
    print(roller_coaster(second_height_list))



