"""
File:    smart_house.py
Author:  Mohiuddin Syed
Date:    11/21/20
Section: 24
E-mail:  msyed2@umbc.edu
Description: ask the user a bunch of question wheter or not they want to add 
devices and etc. user can display what he has chosen, make a file and etc.
"""
class Device:
    def __init__(self, name, toggle):
        self.name = name         # name of the device
        self.toggle = toggle         # tells if the device on or off


class SmartHouse:
    def __init__(self, address):
        self.address = address      # address of the house
        self.device_list = []       # list of the devices
        self.toggleflip = None

    def add_device(self, device):
        self.device_list.append(device)       # add device

    def get_device(self, the_id):
        for device in self.device_list:       # checks all the devices
            if device.name == the_id:         # if device found returns it back
                return device
        return None                           # if found nothing return none

    def save_house(self, file_name):
        savefile = open(file_name, "a")           # appends a file
        for device in self.device_list:
            if device.toggle:                  # If true prints out on
                self.toggleflip = "ON"
                savefile.write(device.name + self.toggleflip + "\n ")
            else:
                self.toggleflip = "OFF"         # if false prints out off
                savefile.write(device.name + self.toggleflip + "\n ")
        savefile.close()

    def load_house(self, file_name):
        loadfile = open(file_name, "r")    # reads the file
        for line in loadfile.readlines():
            x = line.replace("\n").split()     # splits the tab
            if x[1]:                      # if x[1] is true creates a new device
                newDevice = Device(x[0])
                self.add_device(newDevice)

    def display(self):
        print("Address: ", self.address)
        print("Devices")
        for device in self.device_list:        # if statement on and off again
            if device.toggle:
                print('{} : {}'.format(device.name, "ON"))
            else:
                print('{} : {}'.format(device.name, "OFF"))


if __name__ == '__main__':
    address = input('What is the address of the house?')
    house = SmartHouse(address)

    command = input('What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
    while command != 'quit':
        if command == 'add' or command == 'add device':
            the_id = input('What is the device id?')
            if not house.get_device(the_id):
                yes_no = input('Is the device on? (yes/no)')
                if yes_no == 'yes':
                    house.add_device(Device(the_id, True))
                elif yes_no == 'no':
                    house.add_device(Device(the_id, False))
            else:
                print('There is no device id: {} in the ')
        elif command == 'toggle' or command == 'toggle device':
            the_id = input('What is the device id?')
            the_device = house.get_device(the_id)
            if the_device:
                on_off_toggle = input('On, Off or Toggle? ').lower()
                if on_off_toggle == 'on':
                    the_device.toggle = True
                elif on_off_toggle == 'off':
                    the_device.toggle = False
                elif on_off_toggle == 'toggle':
                    the_device.toggle = not the_device.toggle
            else:
                print('There is no device id: {} in the ')
        elif command == 'load':
            file_name = input('What is the filename to load from? ')
            house.load_house(file_name)
            print('The house has been loaded from {}'.format(file_name))
        elif command == 'save':
            file_name = input('What is the filename to save as? ')
            house.save_house(file_name)
            print('The house has been saved in {}'.format(file_name))
        elif command == 'display':
            house.display()
        else:
            print('unknown command', command)

        command = input(
            'What do you want to do? (add device, toggle device, load <file>, save <file>, display) ').lower()
