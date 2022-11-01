"""Project Euler Problem 38 - Pandigital multiples"""


def concatNum(value_a, value_b):
	""" takes two integers and concatenates them, only works for integers > 0

	:param value_a: Int - left integer
	:param value_b: Int - right integer
	:return: Int - both integers concatenated
	"""
	width = len(str(value_b))
	concat = value_a * 10**width + value_b
	return concat


if __name__ == "__main__":
	pandigital_set = {_ for _ in range(1, 10)}
	pandigital_found = []
	for number in range(1, 10_000):
		concatenation = 0
		n = 1
		while len(str(concatenation)) < 9:
			concatenation = concatNum(concatenation, n * number)
			n += 1
		if len(str(concatenation)) == 9:
			iteration_set = {int(digit) for digit in str(concatenation)}
			if iteration_set == pandigital_set:
				pandigital_found.append(concatenation)
	pan = max(pandigital_found)
	print("The largest 1-9 pandigital that is a concatenated product of an integer * (1,2, ..., n) where n > 1:", pan)
