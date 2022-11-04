"""Project Euler Problem 43 - Sub-string divisibility"""


def factorial(number):
	""" simple factorial function, can also use import math for math.factorial() for a faster built in function

	:param number: Int - the number we want to calculate the factorial of
	:return: Int - the final product
	"""
	prod = 1
	for each in range(1, number+1):
		prod *= each
	return prod


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


def concatNum(value_a, value_b):
	""" takes two integers and concatenates them, only works for integers > 0

	:param value_a: Int - left integer
	:param value_b: Int - right integer
	:return: Int - both integers concatenated
	"""
	width = len(str(value_b))
	concat = value_a * 10**width + value_b
	return concat


if __name__ == "__main__":
	prime_list = [2, 3, 5, 7, 11, 13, 17]
	sub_string_pandigitals = []
	# instead of processing the list to exclude numbers with a leading zero we will just slice our
	# list of permutations after the first 9! entries, because our permutations are ordered
	# these are all the leading 0 numbers
	mark = factorial(9)
	p_objects = [_ for _ in range(10)]
	pandigitals = []
	permutation(p_objects, pandigitals, [])
	# main loop
	# for each 0-9 pandigital
	for pandigital_group in pandigitals[mark:]:
		sub_nums = []  # sub numbers for current iteration
		# build the sub_numbers
		# we want 7 sub_strings
		for i in range(1, 8):
			tmp = 0
			# concat the sub_nums
			for digit in pandigital_group[i:i+3]:
				tmp = concatNum(tmp, digit)
			sub_nums.append(tmp)
		# test each sub_num
		flag = False
		# process only exactly as much as needed before abandoning the current iteration
		for i, sub in enumerate(sub_nums):
			if sub % prime_list[i] != 0:
				flag = True
				break
		# if the flag is tripped we move on to the next pandigital group
		if flag:
			continue
		sub_string_pandigitals.append(pandigital_group)
	print(sub_string_pandigitals)
