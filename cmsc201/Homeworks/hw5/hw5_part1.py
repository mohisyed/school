"""
File:         hw5_part1.py
Author:       Mohiuddin Syed
Date:         10/18/2020
Section:      24
E-mail:       msyed2@umbc.edu
Description:  extract the genes between the start and stop codon

"""

import sys
from random import choice, seed


if len(sys.argv) >= 2:
    seed(sys.argv[1])

# USE IF YOU ARE TESTING AND DON'T WANT TO USE COMMAND LINE ARGUMENTS
# seed(input('What seed do you want to use? '))
# END SECTION

STOP_PARAM = 'stop'
SEQ_PARAM = 'seq'
NUCLEOTIDES = ['A', 'T', 'C', 'G']
# your constants should start here
START = ['ATG']
STOP = ['TAA', 'TGA', 'TAG']
CODON_LENGTH = 3


def extract_genes(sequence):
    """
    This function should return a list of genes that start with the
    start codon and end with one of the three stop codons.
    :param sequence: a string of nucleotides
    :return: a list of "genes"
    """
    racker_list: List[Any] = []
    counter = 0
    end = 0
    for i in range(len(sequence)):
        if sequence[i:i+3]in START:   # if sequence from i to i + 3 in start
            counter = i+3
            end = sequence([counter + 3])    # assign the codon

        for x in range(len(end)):
            while end [x:x+3] in STOP:      
                tracker_list.append(sequence: x + 6]))
                return
            
if __name__ == '__main__':
    length_or_stop = input('How many codons do you want to create? (or stop to end, seq to enter your own sequence)')
    while length_or_stop.lower() != STOP_PARAM:
        try:
            if length_or_stop.lower() == SEQ_PARAM:
                the_sequence = input('Enter your own sequence: ').upper()
                if len(the_sequence) % 3 != 0:
                    raise ValueError('The length of the string must be divisible by 3')
                if any(x not in NUCLEOTIDES for x in the_sequence):
                    raise ValueError('The sequence must contain only A, T, C, G')
            else:
                the_sequence = ''.join([choice(NUCLEOTIDES) for _ in range(3 * int(length_or_stop))])
            print(the_sequence)
            print(extract_genes(the_sequence))
        except ValueError:
            print('You entered a non-STOP non-integer, try again. ')
        length_or_stop = input('How many codons do you want to create? (or stop to end, seq to enter your own sequence)')
