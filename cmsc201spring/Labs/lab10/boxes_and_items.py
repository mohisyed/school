"""
File:    boxes_and_items.py
Author:  Mohiuddin Syed
Date:    4/19/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
  creates classes and helpes the user organize them self.
"""

class Box:
    def __init__(self, length, width, height):
        volume = length * width * height
        self.volume = volume
        self.list = []

    def place(self, item):
        if item.volume <= self.volume:
            self.list.append(item)
            self.volume -= item
        else:
            print("no")

    def remove(self, item):
        if item in self.list:
            self.list.remove(item)
            self.volume += item
        else:
            print("its not there")

class Item:
    def __init__(self, length, width, height, name):
        volume = length + width + height + name
        self.volume = volume
        self.name = name

    def place(self, item):
        if item.name not in box.list:
            if box.volume > item.volume:
                box.list.append(item)
        else:
            print("No")

    def remove(self,item):
        if self.name in box.list:
            box.list.remove(item)
            self.volume += Box
        else:
            print("its not there")


if __name__ == '__main__':
    box_list = []
    item_list = []
    command = input('What do you want to do? ')
    while command.strip().lower() != 'quit':
        if command.strip().startswith('create box'):
            try:
                x, y, z = [int(x) for x in command.split()[2:]]
                box_list.append(Box(x, y, z))
            except:
                print('oops probably the wrong number of arguments')
        elif command.strip().startswith('create item'):
            name = command.split()[2]
            try:
                x, y, z = [int(x) for x in command.split()[3:]]
                item_list.append(Item(name, x, y, z))
            except:
                print('oops probably wrong number of arguments')
        elif command.strip().startswith('display boxes'):
            for i, box in enumerate(box_list):
                print("Box {}: with volume {} with {} space left".format(i + 1, box.volume, box.unoccupied_space))
                for item in box_list[i].items:
                    print('\t', item.name, 'is in the box.')
        elif command.strip().startswith('display items'):
            for i, item in enumerate(item_list):
                print("Item {}: with volume {}".format(item.name, item.volume))
        elif command.strip().startswith('place'):
            name_of_item = command.split()[1]
            the_item = None
            for item in item_list:
                if item.name == name_of_item:
                    the_item = item
            number_of_box = int(command.split()[3]) - 1
            if number_of_box in range(len(box_list)) and the_item:
                box_list[number_of_box].place(the_item)
            else:
                print('Error with box number or item name')
        elif command.strip().startswith('remove'):
            name_of_item = command.split()[1]
            the_item = None
            for item in item_list:
                if item.name == name_of_item:
                    the_item = item
            number_of_box = int(command.split()[3]) - 1
            if number_of_box in range(len(box_list)) and the_item:
                box_list[number_of_box].remove(the_item)
            else:
                print('Error with box number or item name')
        command = input('What do you want to do? ')






