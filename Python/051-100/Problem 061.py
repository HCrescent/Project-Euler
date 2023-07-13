"""Project Euler Problem 61 - Cyclical figurate numbers"""
# how I will narrow the search space, do all our grouping of starting 2 digits up front to prevent duplicate checking
# each number 100 times, this will drastically lower our computing time given the upper limit of 30 billion combinations
# we will always start on octagonal because there is the fewest options and thus by assuming the end and
# start of a circle will connect there we can eliminate further combinations from ever checking
# note that we will need to check every other row of matches because we won't know the order of sets in our circle, but
# once a candidate from that set is chosen we should lock out that set from further consideration with a lock flag/mask


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

	print(tensor[10]) # this should if successful show us all candidates for each figurate list starting with 10
	print(tensor[98])
	return tensor


def findCycle(tensor, candidates):
	print(tensor[10])
	flag_mask = 0
	for n, group in enumerate(candidates):
		if group:
			flag_mask ^= 1 << n
	print(bin(flag_mask))
	cycle = []
	return cycle


if __name__ == "__main__":
	figurate_lists = [[], [], [], generateCandidates(3), generateCandidates(4), generateCandidates(5)]
	#hexa_candidates = generateCandidates(6)
	#hepta_candidates = generateCandidates(7)
	#octa_candidates = generateCandidates(8)
	for i, each in enumerate(figurate_lists):
		print(i, each)
	legalTensor(figurate_lists)
	print(figurate_lists)

