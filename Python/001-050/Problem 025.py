"""Project Euler Problem 25 - 1000-digit Fibonacci number"""
# simple with modern python, if I had to deal with integer limits I would use the theoretical infrastructure script
# for large integers mentioned in the Large Sum problem


def n_digit_fibonacci(digits):
	""" Finds the first fibonacci term with n number of digits and returns its index in the sequence (starting from 1)

	:param digits: Int - the number of digits in the term we want to find
	:return: Int - the index (0 exclusive) of the first term with requested length of digits
	"""
	first = 1
	second = 1
	newest = 0
	term_count = 2
	while len(str(newest)) < digits:
		newest = first + second
		first = second
		second = newest
		term_count += 1
	return term_count


if __name__ == "__main__":
	print("The index of the first term in the Fibonacci sequence to contain 1000 digits:", n_digit_fibonacci(1000))
