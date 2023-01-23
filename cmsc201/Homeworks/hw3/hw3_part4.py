"""
File:         hw3_part4.py
Author:       Mohiuddin Syed
Date:         9/26/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  Ask the user how many elements should be in a list. Then the program merges the list

"""
if __name__ == "__main__":
    elements = int(input("How many elements do you want in each list? "))   # defines how many list spots they are
    list1 = []
    list2 = []
    mergedlist = []
    for i in range(elements):
        x = input("What do you want to put in the first list? ")
        list1.append(x)                   # adds the input

    for i in range(elements):
        x = input("What do you want to put in the second list? ")
        list2.append(x)                   # adds the input

    print("the first list is ", list1)
    print("the second list is ", list2)

    for i in range(elements):            # adds the list 1 and list 2 to mergedlist
        mergedlist.append(list1[i])
        mergedlist.append(list2[i])

    print("The merged list is ", mergedlist)
