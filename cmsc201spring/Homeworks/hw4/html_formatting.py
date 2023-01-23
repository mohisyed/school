"""
File:    html_formatting.py
Author:  Mohiuddin Syed
Date:    2/28/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
puts li and ul tags before the user input

"""


li = "</li>\n<li>"


user_input = input("Give me a comma separated list: ")
split_string = user_input.split(",")
li_string = "</li>\n<li>".join(split_string)
li_string = "<ul>\n<li>" + li_string + "</li>\n</ul>"
print(li_string)
