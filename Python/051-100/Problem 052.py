"""Project Euler Problem 52 - Permuted multiples"""


def euler52(bound, multiplicand_height):
	""" find a number where each multiple (in the problem: 2-6) contains the same digits

	:param bound: Int - The upper bound of numbers to search through
	:param multiplicand_height: Int - the number of multiplicands to check against the integer
	:return: Int - The found number, or None type if cant be found
	"""
	for number in range(1, bound):
		accumulator = number
		# sorted string to compare with the numbers multiples
		key = sorted(str(number))
		# for height - 1 because we don't need to process 1 times our number
		for _ in range(multiplicand_height-1):
			# a running accumulation substitutes for multiplication
			accumulator += number
			# if our sorted string is different than our key move on to the next number
			if sorted(str(accumulator)) != key:
				break
		# rare For Else clause, if we hit no breaks we found our answer
		else:
			return number
	return None


if __name__ == "__main__":
	num = euler52(1_000_000, 6)
	print("The smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits is:", num)
