"""Project Euler Problem 60 - Prime pair sets"""


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


def isPrime(value):
	""" Determines if a number is prime, for efficiency’s sake we are only testing values greater than 2
	to avoid edge cases 1 being not prime and 2 being prime

	:param value: Int - Number to check if prime
	:return: Bool - Our truthiness value of prime status
	"""
	# catch even values if driving code doesn't skip 1 or even numbers, and catch negative numbers
	if value % 2 == 0 or value < 2:
		if value == 2:
			return True
		return False
	# our upper range bound is the square root rounded plus 1 to offset the exclusive end of range function
	# the reason for the square root is a shortcut, a whole number factor will never be more than the square root.
	# then for extra efficiency we increment by two to avoid checking even value which will never be a factor of odd#
	for each in range(3, int(value ** .5)+1, 2):
		# if value mod each is zero we found a factor too early, and we know it's not prime
		if value % each == 0:
			return False
	# reaching this line means we never found a factor and its Prime
	return True


def concatNum(value_a, value_b):
	""" takes two integers and concatenates them, inputs are treated as integers not strings
	for example, (1, 0) returns 10, (0, 1) returns 1, (1, 00) returns 10 because 00 == 0

	:param value_a: Int - left integer
	:param value_b: Int - right integer
	:return: Int - both integers concatenated
	"""
	width = len(str(value_b))
	concat = value_a * 10**width + value_b
	return concat


def checkPair(prime_1, prime_2):
	""" takes 2 primes and returns True if they result in a prime when concatenated forwards and backwards

	:param prime_1: Int - prime number
	:param prime_2: Int - prime number
	:return: Bool
	"""
	frontwards = concatNum(prime_1, prime_2)
	backwards = concatNum(prime_2, prime_1)
	width = len(str(frontwards))
	width_cap = len(str(prime_list[-1]))
	if width <= width_cap:  # normal hashable case
		if frontwards in prime_set:
			if backwards in prime_set:
				return True
	else:  # slow un-hashable case
		if isPrime(frontwards):
			if isPrime(backwards):
				return True
	return False


def findSet(primes):
	# first number
	for P1_index, P1 in enumerate(primes):
		# second number
		P2_index = P1_index+1
		for P2 in primes[P1_index+1:]:
			if checkPair(P1, P2):
				# third number
				P3_index = P2_index+1
				for P3 in primes[P2_index+1:]:
					if checkPair(P3, P2) and checkPair(P3, P1):
						# fourth number
						P4_index = P3_index+1
						for P4 in primes[P3_index+1:]:
							if checkPair(P4, P3) and checkPair(P4, P2) and checkPair(P4, P1):
								# fifth number
								# print("tumbler:", P1, P2, P3, P4)
								for P5 in primes[P4_index+1:]:
									# print("test:", P1, P2, P3, P4, P5)
									if checkPair(P5, P4) and checkPair(P5, P3) and checkPair(P5, P2) and checkPair(P5, P1):
										return P1, P2, P3, P4, P5
							P4_index += 1
					P3_index += 1
			P2_index += 1


if __name__ == "__main__":
	prime_list = sieveEratosthenes(1_000_000)
	prime_set = set(prime_list)
	prime_list = sieveEratosthenes(10_000)
	prime_list.pop(0)  # remove 2
	prime_list.pop(1)  # remove 5
	prime_pairs = findSet(prime_list)
	ans = sum(prime_pairs)
	print("The lowest sum for a set of five primes for which any two primes concatenate to produce another prime:", ans)
