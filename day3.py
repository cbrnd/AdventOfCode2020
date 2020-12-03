#-------------------------------------------------------------------------------
# Name:        Advent of Code 2020 / Day 3
# Author:      brand
#-------------------------------------------------------------------------------
import sys

def main():

    slope = getSlope()
    print("Bäme im Weg:\t", check(slope, 3, 1))

    right = [1,3,5,7,1]
    down = [1,1,1,1,2]

    count = 1
    for i in range(len(right)):
        count = count * check(slope, right[i], down[i])

    print("Bäume im Weg: Gesamt:\t", count)

    sys.exit(0)


def check(slope, right, down):

    count = 0
    r = 0
    d = 0

    while d < len(slope) - 1:

        r += right
        d += down

        if slope[d][r % len(slope[d])] == '#':
            count += 1

    return count


def getSlope():

    slope = [list(line.strip('\n')) for line in open('input.txt', 'r')]

    return slope


if __name__ == '__main__':
    main()
