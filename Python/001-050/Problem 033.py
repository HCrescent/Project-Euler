"""Project Euler Problem 33 - Digit cancelling fractions"""


def product(values):
	"""Takes an iterable and creates a product of each element in the iterable

	:param values: List - (or other compatible iterable) to get the product of all elements
	:return: Int - Calculated product
	"""
	prod = 1
	for _ in values:
		prod *= _
	return prod


def primeFactorize(value):
	"""Returns a list of prime factors of given whole number.

	:param value: int - number we are going to factorize
	:return: list - list of prime factors
	"""
	# always check 2 first
	number = 2
	prime_factors = []
	# run until our value is reduced to 1
	while value > 1:
		# always start from the largest prime factor found last
		if len(prime_factors) > 0:
			number = prime_factors[-1]
		# while loop until you hit the first possible divisor, guaranteed to be prime
		# starts at 2 because 1 is not prime and always divisible
		# ends at sqrt of number (if largest factor is itself)
		while number <= value**.5:
			# if number divides evenly
			if value % number == 0:
				# use floored division to prevent expanding int to float
				value //= number
				# append prime factor to list
				prime_factors.append(number)
				# breaks after first prime factor
				break
			# this check is so we can include prime number 2 in our factor checks
			# if LSB of number is 1 we are odd and can skip all the rest of even numbers
			# else move from 2 -> 3
			if number & 1:
				number += 2
			else:
				number += 1
		# since we stopped early to save checking obviously wrong factors
		if number > value**.5:
			# at this point there are no more factors than our leftover value itself
			prime_factors.append(value)
			# lowering value to 1 to prepare to exit function
			value /= value
	return prime_factors


def reduceFraction(numer, denom):
	""" takes a numerator and denominator and reduces it to its simplest form

	:param numer: int - numerator of the rational
	:param denom: int - denominator of the rational
	:return: int, int - the new simplified numerator and denominator
	"""
	# if for some reason we called the function with a zero numerator don't bother calculating
	if numer == 0:
		return 0, 1
	# use prime factorization and canceling like terms to arrive at an irreducible product
	top_factors = primeFactorize(numer)
	bottom_factors = primeFactorize(denom)
	for each in bottom_factors.copy():
		if each in top_factors:
			bottom_factors.remove(each)
			top_factors.remove(each)
	new_numerator = product(top_factors)
	new_denominator = product(bottom_factors)
	return new_numerator, new_denominator


if __name__ == "__main__":
	top_list = []
	bottom_list = []
	# for each 2 digit denominator
	for denominator in range(10, 100):
		# for each 2 digit numerator that makes the rational less than 1
		for numerator in range(10, denominator):
			# split the numerator and denominator into individual digits
			top = [int(_) for _ in str(numerator)]
			bottom = [int(_) for _ in str(denominator)]
			# if the second integer in the split numerator is the same as the first in the denominator
			# then "erroneously" cancel them both
			if top[1] == bottom[0] and bottom[1] != 0:
				if numerator / denominator == top[0] / bottom[1]:
					top_list.append(numerator)
					bottom_list.append(denominator)
					# print(numerator, "/", denominator, "\t", top, "/", bottom)
	final_numerator = product(top_list)
	final_denominator = product(bottom_list)
	final_numerator, final_denominator = reduceFraction(final_numerator, final_denominator)
	print(f"The product of the four fractions given in its lowest common terms: {final_numerator}/{final_denominator}")
