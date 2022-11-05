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
	for Pj in pentagon_list:
		for Pk in pentagon_list:
			if (Pj + Pk) in pentagon_set:
				if abs(Pj - Pk) in pentagon_set:
					Pj_list.append(Pj)
					Pk_list.append(Pk)
	print(Pj_list)
	print(Pk_list)
