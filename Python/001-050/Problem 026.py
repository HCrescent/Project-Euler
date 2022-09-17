"""Project Euler Problem 26 - Reciprocal cycles"""
# solution based on Glaisher 1878, Lehmer 1941 Multiplicative Order and decimal period


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


def decimal_period(value):
	"""Calculates the period of repeating digits in the reciprocal (ex. 1/value) of the given value

	:param value: int - positive number, the denominator in our reciprocal
	:return: int - the period of trailing repeating digits, 0 if decimal terminates
	"""
	factors = primeFactorize(value)
	# our normal theorem is that for any value co-prime to 10 can be used to calculate the repeating period
	# by finding the multiplicative order of 10 % value ( 10**k % value == 1, k is our multiplicative order)
	# remove factors of 2 and 5 to be left with only the factors that can be used to find the decimal period
	factors = [i for i in factors if i != 2 and i != 5]
	# this evaluates true when the only prime factors are 2 and 5 meaning the decimal terminates
	if len(factors) < 1:
		return 0
	# at this point we know that our decimal repeats and our leftover co-prime 10 number can be plugged into
	# the theorem
	number = product(factors)
	exponent = 1
	# this will always find a true evaluation eventually
	while True:
		if 10**exponent % number == 1:
			# we've found our multiplicative order
			return exponent
		exponent += 1


if __name__ == "__main__":
	results = []
	for each in range(1, 1001):
		results.append(decimal_period(each))
	largest = results.index(max(results))+1
	print("The value of d < 1000 for which 1/d contains the longest decimal period is:", largest)
