"""Project Euler Problem 62 - Cubic Permutations"""
from math import log10, ceil

#The Target is the number of exact permutations matches for cubes we want to find
TARGET = 5

def generateCubes():
	""" generator function to generate cubes n^3 from n = 1

	:return: tuple - (int^3, int)
	"""
	num = 1
	while True:
		new = (yield num**3, num)
		if new is not None:
			num = new
		num += 1


if __name__ == "__main__":
	cubes = generateCubes()
	cube_n = cubes.__next__()
	log_target = 0
	highest_found = 0
	solution_list = []
	found_flag = True
	#while we haven't found the target group of cubes
	while found_flag:
		iteration_cube_dict = {}
		# while the generator generates cubes of the log_target digit length
		while ceil(log10(cube_n[0])) <= log_target:
			cube_n = cubes.__next__()
			if ceil(log10(cube_n[0])) == log_target:
				ordered_permutation = tuple(sorted(str(cube_n[0])))
				# if the set of the permutation exists, add the new cube
				if ordered_permutation in iteration_cube_dict:
					iteration_cube_dict[ordered_permutation].append(cube_n)
				else:
					# create first instance
					iteration_cube_dict.update({ordered_permutation: [cube_n]})
		for each in iteration_cube_dict.values():
			if len(each) == TARGET:
				solution_list.extend(each)
				found_flag = False
		log_target += 1

	# out
	solution_list.sort()
	print(f"The smallest cube for which exactly {TARGET} permutations of its digits are cube is: "
	      f"{solution_list[0][0]} ({solution_list[0][1]}³)")
