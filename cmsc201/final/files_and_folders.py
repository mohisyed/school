"""
File:    files_and_folders.py
Author:  Mohiuddin Syed
Date:    12/13/20
Section: 24
E-mail:  msyed2@umbc.edu
Description:
    linux terminal directory in python
"""

class CommandLine:
    def __init__(self):
        self.root = Directory('', None)
        self.current_path = self.root
        self.total_directory = []

    def run(self):
        command = input('>>> ')
        while command.strip().lower() != 'exit':
            split_command = command.split()
            if len(split_command):
                if split_command[0] == 'ls':
                    self.current_path.display()
            if len(split_command) >= 2:
                if split_command[0] == 'cd':
                    self.change_directory(split_command[1])
                elif split_command[0] == 'makedir':
                    self.current_path.create_directory(split_command[1])
                elif split_command[0] == 'fcreate':
                    self.current_path.create_file(split_command[1])
                elif split_command[0] == 'fwrite':
                    self.current_path.file_write(split_command[1])
                elif split_command[0] == 'fread':
                    self.current_path.file_read(split_command[1])
                elif split_command[0] == 'fclose':
                    self.current_path.close_file(split_command[1])
                elif split_command[0] == 'fopen':
                    self.current_path.open_file(split_command[1])

            command = input('>>> ')

    def change_directory(self, dir_name):
        if dir_name not in self.total_directory:
            self.total_directory.append(dir_name)
            print(dir_name, " was made.")
            Directory.parent = dir_name

        Directory.parent = dir_name



class Directory:
    def __init__(self, name, parent):
        self.Commandline = CommandLine
        self.name = name
        self.parent = parent
        self.main_directory = {}
        self.file = None

    def display(self):
        print("ls", "for directory ", self.parent)

    def create_file(self, file_name):    # fix
        self.file[file_name] = [False, []]
        self.parent = self.file

    def create_directory(self, dir_name):
        if self.CommandLine.total_directory is None:
            self.main_directory[dir_name] = {}
            self.parent = self.main_directory[dir_name]
        self.main_directory[dir_name] = {}
        self.parent = self.main_directory[dir_name]

    def file_write(self, file_name):
        input_user = input("What would you like to add? ")
        file_name[1].append("\n ", input_user)

    def file_read(self, file_name):
        print("Contents of the file: ")
        print(file_name[1])

    def close_file(self, file_name):
        if not file_name[0]:
            file_name[0] = False
        else:
            print("File already closed")

    def open_file(self, file_name):
        if not file_name[0]:
            file_name[0] = True
        else:
            print("File already opened")


class File:
    def __init__(self, file_name):
        self.file_name = file_name
    pass


if __name__ == '__main__':
    cmd_line = CommandLine()
    cmd_line.run()
