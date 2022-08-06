"""Project Euler Problem 1"""


def three_or_five(number):
	"""Takes an integer and creates a summation of all natural numbers below given, that are multiples of 3 or 5

	:param number: Int - a natural upper bound (exclusive)
	:return: Int - finished summation
	"""

	summation = 0
	for i in range(number):
		if i % 3 == 0 or i % 5 == 0:
			summation += i
	return summation


if __name__ == "__main__":
	print("The sum of all the multiples of 3 or 5 below 1000 is", three_or_five(1000))
