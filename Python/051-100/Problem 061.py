"""Project Euler Problem 61 - Cyclical figurate numbers"""
from copy import deepcopy

def triangleNumber(n):
	""" returns nth triangle number using formula Tn=n(n+1)/2

	:param n: Int - number 'n'
	:return: Int - triangle number
	"""
	return n*(n+1)//2


def squares(n):
	""" returns nth square number: P4 n = n^2

	:param n: Int - number 'n'
	:return: Int - square number
	"""
	return n*n


def pentagonNumber(n):
	""" return nth pentagonal number with the formula Pn=n(3n−1)/2

	:param n: Int - number 'n'
	:return: Int - nth pentagonal number
	"""
	return n*(3*n-1)//2


def hexagonNumber(n):
	""" return nth hexagonal number with the formula Hn=n(2n−1)

	:param n: Int - number 'n'
	:return: Int - nth hexagonal number
	"""
	return n*(2*n-1)


def heptagonNumber(n):
	""" return nth hexagonal number with the formula P7 n = n(5n - 3)/2

	:param n: Int - number 'n'
	:return: Int - nth heptagonal number
	"""
	return n*(5*n-3)//2


def octagonNumber(n):
	""" return nth hexagonal number with the formula P8 n = n(3n-2)

	:param n: Int - number 'n'
	:return: Int - nth octagonal number
	"""
	return n*(3*n-2)


def generateCandidates(p):
	""" builds a list of 4 digit figurate numbers for p type figurate

	:param p: Int - number that determines which type of figurate to build
	:return: List - all 4 digit figurate numbers of p type
	"""
	match p:
		case 3:
			sequence = triangleNumber
		case 4:
			sequence = squares
		case 5:
			sequence = pentagonNumber
		case 6:
			sequence = hexagonNumber
		case 7:
			sequence = heptagonNumber
		case 8:
			sequence = octagonNumber
		case _:
			print("generateCandidates was given an unmatchable case:", p)
			exit()
	valid_candidates = []
	n = 1
	result = sequence(n)
	while result < 1000:
		n += 1
		result = sequence(n)
	while result < 10000:
		valid_candidates.append(result)
		n += 1
		result = sequence(n)
	return valid_candidates


def legalTensor(candidates):
	""" takes a 2d array of figurate sequences, plugs them into a tensor in order to group them by both figurate and
	the two starting digits

	:param candidates: List - 2d array of figurates
	:return: List - 3d array of the same figurates
	"""
	tensor = [[[] for _ in range(len(candidates))] for _ in range(100)]  # build the empty tensor
	for target in range(10, 100): # for each leading two digits
		for figurate in range(3, len(candidates)):  # for each row of figurate numbers
			while candidates[figurate]:  # while the figurate row is not empty
				if int(str(candidates[figurate][0])[0:2]) != target: # if the test doesn't match move on
					break # move on to next figurate
				else: # else it matches and can be placed into its place in the tensor
					tensor[target][figurate].append(candidates[figurate].pop(0))  # attempt to place into tensor
	return tensor


def findCycle(tensor, candidates):
	""" the main driving function for finding the correct figurate cycle

	:param tensor: List - 3d array of 4 digit figurate numbers by type and leading digits
	:param candidates: List - 2d array of 4 digit figurate numbers by type
	:return: List - the full cycle when found
	"""
	# build the flag bitmask for figurate availability
	flag_mask = 0
	for n, group in enumerate(candidates):
		if group:
			flag_mask ^= 1 << n
	# start logic here (from highest to lowest figurate type)
	for start_f_type in range(3, len(candidates))[::-1]:
		for each in candidates[start_f_type]:
			cycle = [each]
			new_flag_mask = flag_mask ^ (1 << start_f_type)  # toggle starting figurate bit to 0
			target = int(str(each)[-2:])  # target starting digit for the next number in cycle
			result = grabNextRecursive(target, new_flag_mask, tensor, candidates, cycle)
			if len(result) == len(candidates)-3:
				return result


def grabNextRecursive(target, flag_mask, tensor, candidates, cycle):
	""" Recursive function that searches for the next legal number in a potential cycle

	:param target: Int - The last 2 digits of the previous member of the cycle
	:param flag_mask: Int - bitmask for determining which figurate types can still be chosen
	:param tensor: List - 3d list of all the candidates into groups by their leading 2 digits
	:param candidates: List - list of all 4 digits figurates by type
	:param cycle: List - list of members of the cycle so far
	:return: List - list of members of the cycle after processes
	"""
	# end catch
	if len(cycle) == len(candidates) - 3:  # if our cycle is full
		if int(str(cycle[-1])[-2:]) != int(str(cycle[0])[:2]):  # checks if our full cycle is not a true loop
			cycle.pop()  # remove the last element to continue searching
		return cycle  # return the cycle
	# main logic
	for row in range(3, len(candidates)):  # for each figurate row in the target tensor section
		if flag_mask & (1 << row):  # if the row is legal to grab from
			if tensor[target][row]:  # if the row isn't empty
				for new_pick in tensor[target][row]:  # for each available pick we will pick it and recurse
					new_target = int(str(new_pick)[-2:])  # grab target for next recurse
					new_flag_mask = flag_mask ^ (1 << row)  # flag the row as chosen for next recurse
					cycle.append(new_pick)  # append cycle for next recurse
					final_cycle = grabNextRecursive(new_target, new_flag_mask, tensor, candidates, cycle)
					if len(final_cycle) == len(candidates)-3:  # escape clause to climb out of stack
						return final_cycle
	else:  # no continuation was viable for current choice so pop it for replacing on the next go
		cycle.pop()
		return cycle

if __name__ == "__main__":
	figurate_lists = [[], [], []]
	for P in range(3, 9):
		figurate_lists.append(generateCandidates(P))
	solution = findCycle(legalTensor(deepcopy(figurate_lists)), figurate_lists)
	print(solution)
	print("The sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal\n"
	      "type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is:", sum(solution))
