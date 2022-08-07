"""Project Euler Problem 2"""


def fibonacci(bound):
	""" generates the fibonacci sequence and creates a summation of even terms under the upper bound

	:param bound: Int - Our sequence upper bound
	:return: Int - our summation
	"""

	first = 0
	second = 1
	newest = 0
	summation = 0

	while newest < bound:
		newest = first + second
		if not newest & 1:  # use least significant bit to determine even or odd
			summation += newest
		first = second
		second = newest
	return summation


if __name__ == "__main__":
	print("The sum of the even-valued terms of the fibonacci sequence below 4 million: ", fibonacci(4000000))
