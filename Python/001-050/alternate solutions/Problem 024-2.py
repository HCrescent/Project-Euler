"""Project Euler Problem 24 - Lexicographic permutations"""


def factorial(number):
	""" simple factorial function, can also use import math for math.factorial() for a faster built in function

	:param number: Int - the number we want to calculate the factorial of
	:return: Int - the final product
	"""
	product = 1
	for each in range(1, number+1):
		product *= each
	return product


def nth_permutation(objects, target):
	""" calculates the nth lexicographic permutation given a pre-ordered list of objects

	:param objects: List - a list of objects (hopefully ordered) we don't sort in function because it might be odd types
	:param target: int - the index target of all possible permutations in order
	:return: list/string - if function call is out of range return string, otherwise return list for the permutation
	"""
	# catch calls out of range of total number of permutations
	if target > factorial(len(objects)) or target < 1:
		return "out of range"
	permutation = []
	# while we have objects to choose from
	while len(objects) > 0:
		# to figure out the first object slot, calculate how many permutations will pass per choice
		factorial_num = factorial(len(objects)-1)
		# we want only the next lowest integer that will fit wholly, if we use floored division we
		# will get wrong results for divisions that result in whole number naturally
		i = target / factorial_num
		# if the float is a whole number subtract 1
		if i.is_integer():
			i = i-1
		# discard remainder
		i = int(i)
		# subtract skipped iterations from the target
		target -= i * factorial_num
		# append the object to the solution permutation and remove it before looping
		permutation.append(objects[i])
		objects.remove(objects[i])
	return permutation


if __name__ == "__main__":
	N = 1000000
	unique_objects = [_ for _ in range(10)]
	print(f"The {N}(th) lexicographic permutation of", unique_objects.copy(), "is", nth_permutation(unique_objects, N))
