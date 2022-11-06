"""Project Euler Problem 47 - Distinct primes factors"""


def sieveEratosthenes(n):
	""" Generates a list of prime numbers up to inclusive n

	:param n: Int - the upper bound of primes we want
	:return: List - list of prime numbers up to n inclusive
	"""
	# initialize the array for sieving, +1 to keep n included
	numbers = [True for _ in range(n+1)]
	# for 2 through floor of sqrt(n)
	for i in range(2, int(n**.5)+1):
		# if marked True its our next prime
		if numbers[i]:
			# starting at prime squared, run through all multiples marking its composites false
			sub_run = i**2
			# make sure <= to allow n to be flagged appropriately
			while sub_run <= n:
				numbers[sub_run] = False
				sub_run += i
	# list comprehension to convert the boolean array into the meaningful information
	prime_array = [index for index, status in enumerate(numbers) if status]
	# skip 0 and 1 when returning the list
	return prime_array[2:]


def primeFactorize(value):
	"""Returns a list of prime factors of given whole number.

	:param value: int - number we are going to factorize
	:return: list - list of prime factors
	"""
	prime_factors = []
	if value <= 1:
		return prime_factors
	try:
		# prime list exists with all prime numbers possibly needed to factor value
		assert prime_list
	except NameError:
		# prime list doesnt exist
		# always check 2 first
		number = 2
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
	# this section performs the same method as the trial division only
	# without checking any composite numbers by using the pre-calculated prime list
	prime_index = 0
	while prime_list[prime_index] <= value**.5:
		if value % prime_list[prime_index] == 0:
			prime_factors.append(prime_list[prime_index])
			value //= prime_list[prime_index]
			# don't increase the index, start from the last prime divisor
			continue
		prime_index += 1
	# append the final prime factor
	if value > 1:
		prime_factors.append(value)
	return prime_factors


if __name__ == "__main__":
	bound = 1_000_000
	prime_list = sieveEratosthenes(bound)
	unique_factors = []
	for each in range(bound+1):
		# store the number of unique factors at the index of its number
		unique_factors.append(len(set(primeFactorize(each))))
	# width of sliding window
	width = 4
	# adjusted range based on window width
	for i in range(bound-(width-2)):
		# if the set of our current window is the same as our width, then we found the number
		if set(unique_factors[i:i+width]) == {width}:
			break
	# noinspection PyUnboundLocalVariable
	found = i
	print("The first of four consecutive integers to have four distinct prime factors each:", found)
