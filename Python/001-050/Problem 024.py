"""Project Euler Problem 24 - Lexicographic permutations"""
import time
start = time.time()


def permutation(objects, all_permutations, single_permutation):
	# if theres no more elements to choose, append the permutation
	if len(objects) == 0:
		all_permutations.append(single_permutation)
		return all_permutations
	for each in objects:
		new_objects = objects[:]
		current_permutation = single_permutation[:]
		current_permutation.append(each)
		new_objects.remove(each)
		all_permutations = permutation(new_objects, all_permutations, current_permutation)
	return all_permutations


if __name__ == "__main__":
	unique_objects = [_ for _ in range(10)]
	print(unique_objects)
	answers = permutation(unique_objects, [], [])
	print(len(answers))
	print(answers[999999])
	end = time.time()
	total_time = end - start
	print("\n" + str(total_time))
