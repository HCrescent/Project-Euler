"""Project Euler Problem 3 - Largest prime factor"""


def factors(value):
	"""Returns a list of prime factors of given whole number.

	:param value: int - number we are going to factorize
	:return: list - list of prime factors
	"""

	prime_factors = []
	# run until our value is reduced to 1
	while value > 1:
		# for loop until you hit the first possible divisor, guaranteed to be prime
		# starts at 2 because 1 is not prime
		# ends at value (if largest factor is itself), +1 because range() end exclusive bound
		for number in range(2, value + 1):
			# if number divides evenly
			if value % number == 0:
				# use floored division to prevent expanding int to float
				value //= number
				# append prime factor to list
				prime_factors.append(number)
				# breaks after first prime factor
				break
	return prime_factors


if __name__ == "__main__":
	print("Prime factors of given value: ", factors(600851475143))
