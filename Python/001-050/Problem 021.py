"""Project Euler Problem 21 - Amicable numbers"""


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
		# ends at value/2 (if largest factor is itself)
		while number <= value/2:
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
		if number > value/2:
			# at this point there are no more factors than our leftover value itself
			prime_factors.append(value)
			# lowering value to 1 to prepare to exit function
			value /= value
	return prime_factors


def generateDivisors(powers, p_factors, div_list, factor=1, index=0):
	""" Recursive function that generates all divisors of a number given prime factors and their powers

	:param powers: List - an ordered list of power to match with the ordered list of prime factors
	:param p_factors: List - an ordered list of unique prime factors, to be paired with the powers list
	:param div_list: List - our list of discovered divisors
	:param factor: Int - factor to bring through function on our way to make a product for the final divisor
	:param index: Int - index marker for our variable length of expression terms
	:return: List - an updated list of all found divisors to be brought back up the stack and out of the first call
	"""
	# reach the end of our variable length terms we have reached a product that is a divisor
	if index == len(powers):
		# append factor to our list of known divisor, return it up the stack
		div_list.append(factor)
		return div_list
	# for each in the current prime factors power range (ex if power is 2, range we want is 0, 1, 2)
	for each in range(powers[index]+1):
		# calculate the current term raised to (each)
		temp_factor = p_factors[index] ** each
		# multiply it by the factor brought in by the previous function call
		temp_factor *= factor
		# go deeper another call with the new temporary factor, to the next index position
		div_list = generateDivisors(powers, p_factors, div_list, temp_factor, index+1)
	# bring the list of known divisors up the stack
	return div_list


def allDivisors(value):
	""" Prepares the values required to calculate all divisors, passes them to calculate, then formats the result

	:param value: Int - the number we want to find all divisors of
	:return: List - the list of all calculated divisors of value
	"""
	# get the list of prime factors
	prime_factor_list = primeFactorize(value)
	# make a condensed list of unique factors
	unique_prime_factors = list(set(prime_factor_list))
	unique_prime_factors.sort()  # the set function does not retain order so must be re-sorted
	# create a list of the powers of each unique prime factor
	factor_powers = [prime_factor_list.count(_) for _ in unique_prime_factors]
	# call the recursive function to calculate every permutation of prime factor powers product
	divisors_list = generateDivisors(factor_powers, unique_prime_factors, [])
	divisors_list.sort()
	return divisors_list


def properDivisors(value):
	""" Simple variation call for all Divisors, proper divisor excludes value itself

	:param value: Int - The number we want all proper divisors of
	:return: List - return the allDivisors list with the end sliced off (value)
	"""
	return allDivisors(value)[:-1]


if __name__ == "__main__":
	amicable_numbers = []
	for x in range(1, 10000):
		# if true we found a potential amicable pair
		if sum(properDivisors(sum(properDivisors(x)))) == x:
			# make sure its pair isn't actually itself
			if x != sum(properDivisors(x)):
				amicable_numbers.append(x)
	print("The sum of all the amicable numbers under 10000 is", sum(amicable_numbers))
