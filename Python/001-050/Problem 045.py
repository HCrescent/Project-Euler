"""Project Euler Problem 45 - Triangular, pentagonal, and hexagonal"""


def triangleNumber(n):
	""" returns nth triangle number using formula Tn=n(n+1)/2

	:param n: Int - number 'n'
	:return: Int - triangle number
	"""
	return n*(n+1)//2


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


if __name__ == "__main__":
	tri_list = [triangleNumber(_) for _ in range(100_001)]
	penta_set = {pentagonNumber(_) for _ in range(100_001)}
	hexa_set = {hexagonNumber(_) for _ in range(100_001)}
	for i, triangle in enumerate(tri_list[286:]):
		if triangle in penta_set:
			if triangle in hexa_set:
				found = triangleNumber(i+286)
				break
	# noinspection PyUnboundLocalVariable
	print("T285 = P165 = H143 = 40755, the next triangle number that is also pentagonal and hexagonal:", found)
