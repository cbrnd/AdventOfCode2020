#!/usr/bin/env python 3
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        Advent of Code 2020 / Day 1
# Author:      brand
#-------------------------------------------------------------------------------
import sys

def main():

    print("Erster Teil:\t", partOne())
    print("Zweiter Teil:\t", partTwo())
    sys.exit


# Erster Teil der Aufgabe: Zahlenpaar finden und multiplizieren
def partOne():

    amount = 0
    number = getNumbers()

    for i in range(len(number)):
        a = number[i]
        for j in range(len(number)):
            b = number[j]

            if a + b == 2020:
                amount = a * b
                return amount


# Zweiter Teil der Aufgabe: Trio an Zahlen finden und multiplizieren
def partTwo():

    amount = 0
    number = getNumbers()

    for i in range(len(number)):
        a = number[i]
        for j in range(len(number)):
            b = number[j]
            for l in range(len(number)):
                c = number[l]

                if a + b + c == 2020:
                    amount = a * b * c
                    return amount


# Einlesen der Zahlen aus dem File
def getNumbers():

    with open('input.txt', 'r', encoding='UTF-8') as input_file:
        input = input_file.read().split('\n')
        number = []
        for line in input:
            if len(line) > 0:
                number.append(int(line))

    return number


if __name__ == '__main__':
    main()


