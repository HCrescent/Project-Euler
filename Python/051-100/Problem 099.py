"""Project Euler Problem 99 - Largest Exponential"""
from math import log10
with open("text inputs/Problem 099.txt", 'r') as infile:
    data = [list(map(int, line.rstrip().split(','))) for line in infile]


def scaleSort():
    """ Takes large difficult to calculate exponential forms from our input and sorts them to find out which is largest

    :return: Int - the line number at which the largest exponential is written
    """
    results = []
    for number in data:
        results.append(log10(number[0]) * number[1])
    largest = max(results)
    return results.index(largest) + 1


if __name__ == "__main__":
    print("The line of the largest exponential in the file is: ", scaleSort())
