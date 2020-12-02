#!/usr/bin/env python 3
# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        Advent of Code 2020 / Day 2
# Author:      brand
#-------------------------------------------------------------------------------
import sys

def main():

    passwords = getPass()

    print("Part One:")
    print("Anzahl gültiger Passwörter:\t", iterate(passwords, 1), "\n")
    print("Part Two")
    print("Anzahl gültiger Passwörter:\t", iterate(passwords, 2))

    sys.exit(0)


# Alle Einträge durchlaufen
def iterate(entries, version):

    count = 0

    for i in range(len(entries)):

        if splitLine(entries[i], version):
            count = count+1

    return count

# Einen Eintrag in Bestandteile aufteilen
def splitLine(line, version):

    components = line.split(':')
    require = components[0].split(' ')

    borders_str = require[0].split('-')
    character = require[1]
    passcode = components[1]

    borders = []
    borders.append(int(borders_str[0]))
    borders.append(int(borders_str[1]))

    return verify(borders, character, passcode, version)

# Passwort verifizieren, Verifizierungsvariante wird als Parameter mitgegeben
def verify(borders, character, passcode, version):

    if version == 1:
        count = passcode.count(character)

        if count <= borders[1] and count >= borders[0]:
            return True
    else:

        # Index Zero ist aufgrund des Splittens immer ein Leetzeichen!!
        # d.h. es wird nichts am Index verändert
        a = borders[0]
        o = borders[1]

        if (passcode[a] == character) ^ (passcode[o] == character):
                return True


# Einträge aus dem Input-File werden eingelesen
def getPass():

    with open('input.txt', 'r', encoding='UTF-8') as input_file:
        input = input_file.read().split('\n')
        passRequire = []
        for line in input:
            if len(line) > 0:
                passRequire.append(str(line))

    return passRequire


if __name__ == '__main__':
    main()
