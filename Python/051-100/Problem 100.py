"""Project Euler Problem 100 - Arranged Probability"""
from math import sqrt

def quadraticFormula(a, b, c):
    radical = sqrt(b**2 - (4 * a * c))
    denominator = 2 * a
    solution1 = -1 * b + radical
    solution1 /= denominator
    solution2 = -1 * b - radical
    solution2 /= denominator
    return solution1, solution2


if __name__ == "__main__":
    n = 1
    solutions = {}
    for each in range(1_000_000_000_000, 1_000_000_100_001):
        result  = quadraticFormula(1,-1, -1 * ((each**2 - each)/2))
        if result[0].is_integer() and result[1].is_integer():
            solutions.update({each: result})
    for i, each in enumerate(solutions):
        print("solution number: ", i, "N: ", each, "|blue discs: ", solutions[each])
    print(quadraticFormula(1, -1, -1 * ((21 * 20)/2)))

