"""Project Euler Problem 21 - Amicable numbers"""
# In the original tackling of this problem I generated all divisors for each tested number
# because I liked that you could instantly calculate those out on wolfram alpha so I wanted to learn how
# Turns out for The sum of divisors you don't actually need to generate all the factors to sum them up
# there is a nice formula for σ(prime^power) = (prime^power+1 - 1)/(prime-1)


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


if __name__ == "__main__":
	amicable_numbers = []
	for x in range(10000):
		# if true we found a potential amicable pair
		if aliquotSum(aliquotSum(x)) == x:
			# make sure its pair isn't actually itself
			# with the current formula, we must check x > 1 because if we plug in σ(σ(1)) we end up with σ(0) which due
			# to the product function returns 1 resulting in a false flag that one is an amicable number (σ(1) = 0, σ(0) = 1)
			# that is then not caught by the perfect number catch because σ(0) returns 1 when it should be undefined
			# but we already use an empty list for "prime factors" of 1
			if x != aliquotSum(x) and x > 1:
				amicable_numbers.append(x)
	print("The sum of all the amicable numbers under 10000 is", sum(amicable_numbers))
