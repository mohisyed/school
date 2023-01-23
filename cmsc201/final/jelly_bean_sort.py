"""
File:    jelly_bean_sort.py
Author:  Mohiuddin Syed
Date:    12/13/20
Section: 24
E-mail:  msyed2@umbc.edu
Description:
    to sort the jellybeans and tell how many of each color they're
"""


def bubble_simple_sort(my_list):
    for i in range(len(my_list)-1):
        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

def jelly_bean_sort(list_of_colors):
    # Count the colors here
    count_dict = {}
    for item in list_of_colors:
        if item in count_dict:  # Check if already present
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Get the key value and sort it
    sorted_list = bubble_simple_sort(list(count_dict.items()))
    return sorted_list


colors = ['red', 'green', 'red', 'yellow', 'green', 'red', 'blue', 'red', 'green', 'yellow']
print(jelly_bean_sort(colors))
