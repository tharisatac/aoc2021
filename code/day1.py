
from os import read


def read_input():
    """ Read input file """
    with open('inputs/day1.txt') as f:
        lines = f.read().splitlines()

    for line in lines:
        yield int(line)

def find_measurements_larger_than_prev():
    """ Find all measurements greater than previous measurements"""

    counter = -1
    prev = 0
    for num in read_input():
        # First prev is always less than num
        if prev < num:
            counter += 1
            prev = num
        else:
            prev = num

    print(counter)

find_measurements_larger_than_prev()