#!/usr/bin/python
#-------------------------------------------------------------------------------
# Name:        Advent of Code 2020
# Author:      brand
#-------------------------------------------------------------------------------
import string

def main():

    values = [i.strip('\n') for i in open('input.txt', 'r')]

    seats = []
    for value in values:
        id = ''.join([('0' if i in ['F', 'L'] else '1') for i in value])
        seats.append(int(id[:7], 2) * 8 + int(id[7:], 2))

    print('Highest seat ID: ', max(seats))
    print('My seat ID: ', set(range(min(seats), max(seats))) - set(seats))


if __name__ == '__main__':
    main()
