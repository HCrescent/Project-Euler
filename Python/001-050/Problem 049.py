"""Project Euler Problem 49 - Prime permutations"""


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


def permutation(objects, all_permutations, single_permutation):
	""" Generates all permutations of a given list of objects of any mix of types, if the list is ordered before
	calling, then the list of all permutations will be lexicographic (in sorted order)

	:param objects: List - list of objects to generate permutations of, if the list is ordered, it will be lexicographic
	:param all_permutations: List - the master list of all generated permutations
	:param single_permutation: List - the in progress permutation
	:return: None - because our list of permutations is passed by reference we don't actually need to return it
	"""
	# if theres no more objects to choose from, append the finished permutation
	if len(objects) == 0:
		all_permutations.append(single_permutation)
		return
	# for each object in the list received
	for each in objects:
		# create copies to avoid passing by reference because when we return up the stack we
		# don't want those to be changed by lower levels
		new_objects = objects.copy()
		current_permutation = single_permutation.copy()
		# add to the current in progress permutation and remove that same object from the copied list for the
		# next layer down
		current_permutation.append(each)
		new_objects.remove(each)
		# call next layer
		permutation(new_objects, all_permutations, current_permutation)
	return


if __name__ == "__main__":
	prime_list = sieveEratosthenes(10_000)
	# narrow the list to only 4 digit primes
	prime_list = [_ for _ in prime_list if len(str(_)) == 4]
	# prime set for containment comparisons
	prime_set = set(prime_list)
	solution_set = set()
	# because the question was ambiguous that the arithmetic sequence was going to use same difference
	# this section is written with extra searching as if the difference was unknown
	for each in prime_list:
		# split the primes digits into separate objects for permutation
		prime_digits = list(str(each))
		# build permutations of the prime number
		prime_permutations = []
		permutation(prime_digits, prime_permutations, [])
		# convert the permutations into their proper integer form with set comprehension
		prime_permutations_set = {int("".join(_)) for _ in prime_permutations}
		# use intersection of sets to remove any non-prime permutations
		prime_permutations_set = prime_permutations_set & prime_set
		# create a list of the set for sorted iteration to find the difference in the arithmetic sequence of primes
		prime_permutations = list(prime_permutations_set)
		prime_permutations.sort()
		# for each prime number Pj in the permutations, find the difference with Pk
		for i, Pj in enumerate(prime_permutations):
			for Pk in prime_permutations[i+1:]:
				tmp_diff = abs(Pj - Pk)
				# now take that difference and add it to Pk, if the result is in the permutations we found a solution
				if Pk + tmp_diff in prime_permutations_set:
					solution_set.add(int(str(Pj) + str(Pk) + str(Pk+tmp_diff)))
	solution_set.remove(148748178147)  # remove the given element from the question
	print("The 12-digit number formed by concatenating the three terms in this sequence:", solution_set.pop())
