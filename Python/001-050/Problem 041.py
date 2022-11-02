"""Project Euler Problem 41 - Pandigital prime"""


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
	found_prime = 0
	# going from largest to smallest scope for pandigital primes
	for scope in range(2, 10)[::-1]:
		# get ready to generate all pandigital permutations for current scope
		numbers = [str(_) for _ in range(1, scope)]
		# filter to narrow our scope further because we are going to be using a somewhat slow primality check
		filter_set = {'1', '3', '7', '9'}
		permutation_list = []
		potential_primes_list = []
		# generate permutation list
		permutation(numbers, permutation_list, [])
		# eliminate all obviously non-prime permutations, add potentials to new list as an integer
		for index, digit_list in enumerate(permutation_list):
			# if the last digit is not indicative of a composite
			if digit_list[-1] in filter_set:
				potential_primes_list.append(int("".join(digit_list)))
		# check narrowed scope of potentially prime numbers starting from largest to lowest
		# because our permutations were lexicographic we can process in reverse order
		for each in potential_primes_list[::-1]:
			if isPrime(each):
				found_prime = each
				# break at the first True for is Prime, found target
				break
		# if we found our target skip the rest of remaining scope
		if found_prime:
			break
	print("The largest n-digit pandigital prime that exists:", found_prime)
