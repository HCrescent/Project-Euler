"""Project Euler Problem 24 - Lexicographic permutations"""


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
	nth_permutation = 1000000
	unique_objects = [_ for _ in range(10)]
	answers = []
	permutation(unique_objects, answers, [])
	print("The 1000000th lexicographic permutation of", unique_objects, "is", answers[nth_permutation-1])
