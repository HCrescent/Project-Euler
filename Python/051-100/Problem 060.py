"""Project Euler Problem 60 - Prime pair sets"""
from itertools import combinations


# quick abstract, find the smallest sum of a set of 5 primes, where every permutation of 5 choose 2 results in a prime
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


def factorial(number):
	""" simple factorial function, can also use import math for math.factorial() for a faster built in function

	:param number: Int - the number we want to calculate the factorial of
	:return: Int - the final product
	"""
	prod = 1
	for each in range(1, number+1):
		prod *= each
	return prod


def combinatorics(n, k):
	""" Simple combinatorics formula for n choose k, n! / k!(n-k)!


	:param n: Int - Number to choose from
	:param k: Int - total of choices
	:return: Int - the solution to formula n! / k!(n-k)!
	"""
	numerator = factorial(n)
	denominator = factorial(k) * factorial(n - k)
	return numerator // denominator


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


def createCombinations(objects, limit):
	comb_list = []
	for i, P1 in enumerate(objects[:limit]):
		for P2 in objects[i+1:limit]:
			# check width to catch concatenations larger than our prime sieve
			# these cases will be checked without hashtable
			frontwards = concatNum(P1, P2)
			backwards = concatNum(P2, P1)
			width = len(str(frontwards))
			width_cap = len(str(prime_list[-1]))
			if width <= width_cap:  # normal hashable case
				if frontwards in prime_set:
					if backwards in prime_set:
						comb_list.append((P1, P2))
			else:  # slow un-hashable case
				if isPrime(frontwards):
					if isPrime(backwards):
						comb_list.append((P1, P2))
	return comb_list


def narrowDown():
	set_size = 5
	pair_list = createCombinations(prime_list, 200)
	pair_set = set(pair_list)
	flatten = [each for coord in pair_list for each in coord]
	candidate_set = set([each for each in flatten if flatten.count(each) > 3])
	candidate_list = list(sorted(candidate_set))
	print("candidates:", len(candidate_list))
	print("total combinations:", combinatorics(len(candidate_list), set_size))
	gen_comb = combinations(candidate_list, set_size)
	not_found = True
	test_count = 0
	while not_found:
		cur_test = next(gen_comb)
		test_gen = combinations(cur_test, 2)
		for coord in test_gen:
			if coord not in pair_set:
				break
		else:  # reach here and you passed all tests and found the answer
			return cur_test
		test_count += 1
		if test_count % 100_000_000 == 0:
			print(test_count)
	return


if __name__ == "__main__":
	prime_list = sieveEratosthenes(1_000_000)
	prime_list.pop(0)
	prime_set = set(prime_list)
	print("largest prime = ", prime_list[-1])
	print("prime list length:", len(prime_list))
	print(narrowDown())
