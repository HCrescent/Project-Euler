"""Project Euler Problem 15 - Lattice paths"""


def factorial(number):
	""" simple factorial function, can also use import math for math.factorial() for a faster built-in function

	:param number: Int - the number we want to calculate the factorial of
	:return: Int - the final product
	"""
	product = 1
	for each in range(1, number+1):
		product *= each
	return product


def combinatorics(n, k):
	""" Simple combinatorics formula for n choose k, n! / k!(n-k)!
	This approach works for the problem because any route from one corner of a grid to the opposite corner is going
	to be for grid size k, k right moves, and k left moves, in every combination of possibilities to slot into
	n = 2k moves total, every possible way you can slot 20 identical moves into 40 total (the other 20 moves go in
	the leftover vacant slots)

	:param n: Int - Number to choose from
	:param k: Int - total of choices
	:return: Int - the solution to formula n! / k!(n-k)!
	"""
	numerator = factorial(n)
	denominator = factorial(k) * factorial(n - k)
	return numerator // denominator


if __name__ == "__main__":
	print("The number of routes with only right and down turns of a 20 by 20 grid:", combinatorics(40, 20))
