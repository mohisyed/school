"""
File:   russian_dolls.py
Author:  Mohiuddin Syed
Date:    4/21/21
Section: 31
E-mail:  msyed2@umbc.edu
Description:
recusvily find the russian dolls how many

"""

def russian_dolls(n):
    if n == 1:   # base case if n = 1
        return 1
    if n % 2 == 0:    # if equals even
        return 2 * russian_dolls(n / 2) + 1
    else: # if odd
        return russian_dolls(n // 2) + russian_dolls((n // 2) + 1) + 1



if __name__ == '__main__':
    print(russian_dolls(5))
    print(russian_dolls(1))
    print(russian_dolls(4))
    print(russian_dolls(17))
