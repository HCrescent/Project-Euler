"""Project Euler Problem 35 - Circular primes"""


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


def barrelRotate(value):
	"""Takes a number and returns a list of all barrel rotations of that number (shifting without losing digits)

	:param value: Int - value we want to rotate
	:return: List - all rotations of that number
	"""
	# create a list of characters of the value
	number_list = [_ for _ in str(value)]
	len_digits = len(number_list)
	rotation_list = []
	# for the number of rotations needed
	for _ in range(len_digits):
		# take the character at position zero, pop it and put it onto the end of the list
		number_list.append(number_list.pop(0))
		# change back to an integer from list of characters
		rotation_list.append(int("".join([_ for _ in number_list])))
	return rotation_list


def circularPrimes(bound):
	"""creates a list of circular primes (primes which are prime in every barrel shifted form)

	:param bound: Int - inclusive upper bound
	:return: List - list of circular primes
	"""
	# all circular primes more than 1 digit must contain only numbers in this set
	circular_set = {1, 3, 7, 9}
	# generate prime numbers
	primes = sieveEratosthenes(bound)
	# all single digit primes are circular primes
	circular_primes = primes[:4]
	circular_potentials = []
	for each in primes[4:]:
		temp_set = {int(_) for _ in str(each)}
		# if a prime number contains any numbers not in our circular set, we get the empty set
		# and it is a candidate for being a circular prime
		if temp_set.difference(circular_set) == set():
			circular_potentials.append(each)
	# now that the search has been narrowed, we can process all rotations for primality
	rotations_list = [barrelRotate(each) for each in circular_potentials]
	for index, group in enumerate(rotations_list):
		for number in group:
			if primes.count(number) < 1:
				circular_potentials[index] = None
				break  # break out of processing this group
	[circular_primes.append(_) for _ in circular_potentials if _]
	return circular_primes


if __name__ == "__main__":
	print(circularPrimes(1000000))
