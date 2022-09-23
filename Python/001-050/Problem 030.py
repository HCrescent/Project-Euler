"""Project Euler Problem 30 - Digit fifth powers"""


def sum_of_digit_powers(exponent):
	""" finds numbers that are the sum of their individual digits raised to a given power
	note for increasing exponents algorithm drops off hard and would require a new method
	:param exponent: int - the exponent we want to use on digits in the sum
	:return: list - a list of found numbers that are equal to the sum of digits raised to the exponent
	"""
	digits = 1
	perfect_digital_invariants = []
	# we can be sure that it is impossible to find numbers that fit beyond a limit
	# where the number of digits times 9^exponent is smaller than the number of digits in our range to check
	while len(str(10**digits)) <= len(str((9**exponent) * digits)):
		digits += 1
	# the new upper limit can be now be (9**exponent) * digits because one more than that would require
	# an extra digit of powers
	for each in range(2, ((9**exponent) * digits)+1):
		# list comprehension to split an integer into a string of digits converting them back to integers to be
		# raised to an exponent before summing them up
		if sum([int(x)**exponent for x in str(each)]) == each:
			perfect_digital_invariants.append(each)
	return perfect_digital_invariants


if __name__ == "__main__":
	answers = sum_of_digit_powers(5)
	print("The sum of all the numbers that can be written as the sum of fifth powers of their digit is", sum(answers))
