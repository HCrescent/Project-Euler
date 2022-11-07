"""Project Euler Problem 44 - Pentagon numbers"""


def pentagonNumber(n):
	""" return nth pentagonal number with the formula Pn=n(3n−1)/2

	:param n: Int - number 'n'
	:return: Int - nth pentagonal number
	"""
	return n*(3*n-1)//2


if __name__ == "__main__":
	pentagon_list = [pentagonNumber(_) for _ in range(1, 10001)]
	pentagon_set = set(pentagon_list)
	Pj_list = []
	Pk_list = []
	for i, Pj in enumerate(pentagon_list):
		# start at i+1 to prevent duplicate checking ex. we already check 1, 5 we don't need to check 5, 1
		# so starting from i+1 we eliminate checking 1 against any number as it would already have been done
		for Pk in pentagon_list[i+1:]:
			if Pj + Pk in pentagon_set:
				if abs(Pj - Pk) in pentagon_set:
					Pj_list.append(Pj)
					Pk_list.append(Pk)
	# there ended up being only one found, but we didn't know that ahead of time so well leave the
	# declaration at the start as lists
	D = abs(Pj_list[0] - Pk_list[0])
	print("For 2 pentagonal number Pj and Pk, for which sum and difference is pentagonal D = |Pj - Pk|. D:", D)
