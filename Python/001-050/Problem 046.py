"""Project Euler Problem 46 - Goldbach's other conjecture"""


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


if __name__ == "__main__":
	bound = 10000
	# build primes
	prime_list = sieveEratosthenes(bound)
	prime_set = set(prime_list)
	# build odd non-primes
	odd_composite_list = [_ for _ in range(3, bound, 2) if _ not in prime_set]
	# we are going to be checking for composites in the list so make a set for it O(1) vs O(N)
	odd_composite_set = set(odd_composite_list)
	# build a list of squares
	squares_list = [_**2 for _ in range(1, (int(bound**.5))+1)]
	# crunch every prime + 2*square possible and remove the result from the set
	for prime in prime_list:
		for square in squares_list:
			# we might get answers outside of the range so using try:except: to handle key errors
			try:
				odd_composite_set.remove(prime+(2*square))
			except KeyError:
				continue
	if len(odd_composite_set) > 0:
		found = min(list(odd_composite_set))
		print("The smallest odd composite that cannot be written as the sum of a prime and twice a square:", found)
