"""Project Euler Problem 37 - Truncatable primes"""


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


def numTruncate(number, mode):
	""" Takes a number and creates a list of truncated version of the given number
	Modes are L for left-to-right truncation, R for right-to-left truncation, and B for both L and R

	:param number: Int - Integer we want to truncate
	:param mode: Str - Mode indicator, supports only L, R, or B
	:return: Set - set of requested truncations of given number
	"""
	# make sure the proper modes are called
	try:
		assert mode in {'L', 'R', 'B'}
	except AssertionError:
		raise AssertionError(f"An invalid mode was received: ({number}, {mode}) needs L R or B for mode")
	# technically log10 would be faster but the difference is extremely negligible for our purposes
	# and this requires no edge case for 0 so its simpler
	width = len(str(number))
	trunc_set = {number}
	if mode in {'L', 'B'}:
		for magnitude in range(width):
			# shave the leftmost digit off
			trunc_set.add(number - (number // 10**(magnitude+1)) * 10**(magnitude+1))
	if mode in {'R', 'B'}:
		for magnitude in range(width):
			# shave the rightmost digit off
			trunc_set.add(number // 10**magnitude)
	return trunc_set


if __name__ == "__main__":
	prime_list = sieveEratosthenes(1000000)
	prime_set = set(prime_list)
	truncatable_primes = []
	# The problem dictates that single digit primes are not eligible as Truncatable Primes
	for each in prime_list[4:]:
		# set logic, if the set we get from our function is a subset of prime_set all its members are prime
		if numTruncate(each, 'B') <= prime_set:
			truncatable_primes.append(each)
		# stop processing once we found all of them (according to project euler there is only 11 that exist)
		if len(truncatable_primes) == 11:
			break
	total = sum(truncatable_primes)
	print("The sum of the only eleven primes that are both truncatable from left to right and right to left:", total)
