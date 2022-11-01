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
	:return: Set - set of
	"""
	# make sure the proper modes are called
	try:
		assert mode in ('L', 'R', 'B')
	except AssertionError:
		raise AssertionError(f"An invalid mode was received: ({number}, {mode}) needs L R or B for mode")
	from math import log10
	width = int(log10(number))+1
	trunc_set = {number}
	if mode == 'L' or mode == 'B':
		for magnitudeL in range(width):
			trunc_set.add(number - (number // 10**(magnitudeL+1)) * 10**(magnitudeL+1))
	if mode == 'R' or mode == 'B':
		for magnitude in range(width):
			trunc_set.add(number // 10**magnitude)
	return trunc_set


if __name__ == "__main__":
	prime_list = sieveEratosthenes(100)
	prime_set = set(prime_list)
	# for each in prime_list:
	print('L:', numTruncate(37, 'L'))
	print('R:', numTruncate(37, 'R'))
	print('B:', numTruncate(37, 'B'))
