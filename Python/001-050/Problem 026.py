"""Project Euler Problem 26 - Reciprocal cycles"""


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


def reciprocal_repeating(value):
	""" evaluates if a value has a repeating decimal in its reciprocal (1/value)

	:param value: the denominator in the reciprocal
	:return: bool - True if the decimal
	"""
	factors = primeFactorize(value)
	# if the factors are all 2's and/or 5's return false
	return factors.count(2) + factors.count(5) != len(factors)


def decimal_period(value):
	if not reciprocal_repeating(value):
		return 0
	factors = primeFactorize(value)
	factors = [i for i in factors if i != 2 and i != 5]
	number = product(factors)
	exponent = 1
	while True:
		if 10**exponent % number == 1:
			return exponent
		exponent += 1


if __name__ == "__main__":
	results = []
	for each in range(1, 1001):
		results.append(decimal_period(each))
	largest = results.index(max(results))+1
	print(largest, "repeating digits:", results[largest-1])
