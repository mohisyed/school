"""
File:    Down_The_Path.py
Author:  Mohiuddin Syed
Date:    10/6/20
Section: 24
E-mail:  msyed2@umbc.edu
Description:  prints the recursive formula

"""


def count_down(count):
    if count <= 0:
        return 0
    else:
        return 1 + count_down(count - 1)


def down_the_path(n):
    """
   :param n: an integer
   :return: the number of times that down the path runs
   """
    if n <= 0:     # integer less than equal 0
        return 0
    elif n % 15 == 0:   # modulo division 15
        return 1 + down_the_path(n / 15)
    elif n % 5 == 0:    # modulo division 5
        return 1 + down_the_path(n / 5)
    elif n % 3 == 0:    # modulo division 3
        return 1 + down_the_path(n / 3)
    elif n > 0:         # greater than 0
        return 1 + down_the_path(n - 1)


if __name__ == '__main__':
    for i in range(20):
        print(i, down_the_path(i))
