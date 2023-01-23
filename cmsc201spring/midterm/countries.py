"""
File:    countires.py
Author:  Mohiuddin Syed
Date:    4/26/21
Section: 31
E-mail:  msyed2@umbc.edu
Description: 
    reads the csv file and tells the info
"""

small_countries = "small_countries.csv"
big_countries = "big_countries.csv"


def file_checker(csv_file):
    if csv_file == small_countries:
        f = open("small_countries.txt", "r")
        return f
    elif csv_file == big_countries:
        return open("big_countries.txt", "r")
        return f


def read_line(files):
    a = 3
    while a == 3:
        r = files.readline().split()
        if len(r) != 4:
            a = 0
    else:
        file_dict[r[0]] = r[1:]
        return file_dict


if __name__ == '__main__':
    file_dict = {}
    fname = input("What is the file name of the country data? ")

    file = file_checker(fname).read()
    read = read_line(file)

    command = ""
    flag = "quit"
    while command != flag:
        command = input("Enter command: ")
        splits = command.split()
        if len(splits) == 2 and splits[0] == "display":
            print("Information for ", splits[1])
        print(" Land area: ", file_dict[splits[1]][0])
        print(" Population: ", file_dict[splits[1]][1])
        print(" GDP: ", file_dict[splits[1]][2])

        if len(splits) == 3 and splits[0] == "display":
            for k in dict.keys():
                print(k, end=", ")
        elif len(splits) == 3 and splits[0] == "compare":
            print("Comparision of ", splits[1], " with ", splits[2])

        if file_dict[splits[1]][0] > file_dict[splits[2]][0]:
            print("Land area of ", splits[1], " is bigger than ", splits[2])
        else:
            print("Land area of ", splits[2], " is bigger than ", splits[1])

        if file_dict[splits[1]][1] > file_dict[splits[2]][1]:
            print("Population of ", splits[1], " is bigger than ", splits[2])
        else:
            print("Population of ", splits[2], " is bigger than ", splits[1])
        if file_dict[splits[1]][2] > file_dict[splits[2]][2]:
            print("GDP of ", splits[1], " is bigger than ", splits[2])
        else:
            print("GDP of ", splits[2], " is bigger than ", splits[1])
