"""Project Euler Problem 1 - Multiples of 3 or 5"""


def sumDivisibleBy(number, bound=1000):
	"""Takes an integer and creates a summation of all natural numbers below given, that are multiples of 3 or 5
	the summation of integers from 1 to bound = .5*n*(n+1)
	instead we are making a summation of multiples of number from number to bound, then we can pull number out
	of that series resulting in a formula of number*.5*n*(n+1) for an updated bound of bound//number

	:param number: Int - what numbers divisors are in the natural numbers below the bound
	:param bound: Int - a natural upper bound (exclusive)
	:return: Int - finished summation
	"""
	# bound - 1 because we are only counting number BELOW the bound
	n = (bound - 1) // number
	return number * (n * (n + 1)) // 2


if __name__ == "__main__":
	# the because multiples of both 3 and 5 are counted twice we must subtract those numbers counted twice (3*5)
	print("The sum of multiples of 3 or 5 below 1000 is:", sumDivisibleBy(3) + sumDivisibleBy(5) - sumDivisibleBy(15))
