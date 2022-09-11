"""Project Euler Problem 23 - Non-abundant sums"""


def product(values):
	"""Takes an iterable and creates a product of each element in the iterable

	:param values: List - (or other compatible iterable) to get the product of all elements
	:return: Int - Calculated product
	"""
	prod = 1
	for each in values:
		prod *= each
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


def divisorsSum(value):
	# get the list of prime factors
	prime_factor_list = primeFactorize(value)
	# make a condensed list of unique factors
	unique_prime_factors = list(set(prime_factor_list))
	unique_prime_factors.sort()  # the set function does not retain order so must be re-sorted
	# create a list of the powers of each unique prime factor
	factor_powers = [prime_factor_list.count(_) for _ in unique_prime_factors]
	# because we don't know how many prime factors a given number might arbitrarily have
	# we will generate all the numerator terms and the denominator terms in a list separately
	# because individually the division will result in various levels of float precision
	# that when multiplied together will produce imprecise results
	# but we know when all the terms in the numerators are multiplied together and all the terms of the denominators
	# are multiplied together we will end up with a division with whole number answers
	# so we avoid doing the division to till the last step
	numerators = [(prime**(factor_powers[i]+1))-1 for i, prime in enumerate(unique_prime_factors)]
	denominators = [prime-1 for prime in unique_prime_factors]
	# floored division operator to get rid of the float type (we will never have decimal answers)
	return product(numerators)//product(denominators)


def aliquotSum(value):
	"""Alternate call of the divisors sum function to exclude value itself from the sum

	:param value: Int - Value to calculate aliquot sum of
	:return: Int - Divisor sum excluding value itself
	"""
	return divisorsSum(value) - value


def generateAbundantNumbers(upper_bound):
	""" Generates a list of abundant numbers (such that the aliquot sum of a number N is greater than N

	:param upper_bound: Int - the upper limit for the generator
	:return: List - all abundant numbers requested
	"""
	abundant_numbers = []
	for each in range(1, upper_bound+1):
		if each < aliquotSum(each):
			abundant_numbers.append(each)
	return abundant_numbers


if __name__ == "__main__":
	bound = 28123
	# generate a list of abundant numbers
	temp_list = generateAbundantNumbers(bound)
	# create an empty set
	sum_of_2_abundant_numbers = set()
	for abundant in temp_list:
		# skip abundant numbers greater than half our bound as they would produce integers outside our bound
		if abundant * 2 > bound:
			break
		for abundant2 in temp_list:
			# generate a set of each integer that can be the sum of two abundant numbers (up to the bound)
			sum_of_2_abundant_numbers.add(abundant + abundant2)
	# generate a set of all positive integers up to the bound
	answer_set = set(range(1, bound + 1))
	# use set subtraction to get all the numbers that CAN NOT be the sum of two abundant numbers
	answer_set = answer_set - sum_of_2_abundant_numbers
	print("The Σ of all positive integers that can't be written as the sum of two abundant numbers is", sum(answer_set))
