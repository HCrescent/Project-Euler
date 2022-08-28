"""Project Euler Problem 14 - Longest Collatz sequence"""
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)


def longestCollatzSequence(bound=1000000):
	""" iteratively generates collatz sequences, checks how long they were and indexes the length

	:param bound: Int - The upper limit for our seeding number
	:return: Int - index of the max value, add one and that's our best performing seed
	"""
	collatz_lengths = []
	for each in range(1, bound):
		temp_sequence = [each]
		while each > 1:
			# if odd (LSB check)
			if each & 1:
				each = 3 * each + 1
			# if even
			else:
				each //= 2
			temp_sequence.append(each)
		collatz_lengths.append(len(temp_sequence))
	return collatz_lengths.index(max(collatz_lengths)) + 1


if __name__ == "__main__":
	print("The starting number, under one million, produces the longest Collatz sequence is:", longestCollatzSequence())
