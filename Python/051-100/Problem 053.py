"""Project Euler Problem 53 - Combinatoric selections"""


def factorial(number):
	""" simple factorial function, can also use import math for math.factorial() for a faster built in function

	:param number: Int - the number we want to calculate the factorial of
	:return: Int - the final product
	"""
	prod = 1
	for each in range(1, number+1):
		prod *= each
	return prod


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
	counter = 0
	for N in range(1, 101):
		for R in range(1, N+1):
			if combinatorics(N, R) > 1_000_000:
				counter += 1
	print("The total number of values of (n choose k) for 1 <= n <= 100, that are greater than one-million:", counter)
