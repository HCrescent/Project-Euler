"""Project Euler Problem 58 - Spiral primes"""


def isPrime(value):
	""" Determines if a number is prime, for efficiency’s sake we are only testing values greater than 2
	to avoid edge cases 1 being not prime and 2 being prime

	:param value: Int - Number to check if prime
	:return: Bool - Our truthiness value of prime status
	"""
	# catch even values if driving code doesn't skip 1 or even numbers, and catch negative numbers
	if value % 2 == 0 or value < 2:
		if value == 2:
			return True
		return False
	# our upper range bound is the square root rounded plus 1 to offset the exclusive end of range function
	# the reason for the square root is a shortcut, a whole number factor will never be more than the square root.
	# then for extra efficiency we increment by two to avoid checking even value which will never be a factor of odd#
	for each in range(3, int(value ** .5)+1, 2):
		# if value mod each is zero we found a factor too early, and we know it's not prime
		if value % each == 0:
			return False
	# reaching this line means we never found a factor and its Prime
	return True


def spiral_matrix(percentage):
	""" alteration of the function used in problem 28, changed to analyze the corners instead of sum them.

	:param percentage: the threshold ratio of primes to total numbers we are looking for
	:return: Int - width of the spiral square at target threshold
	"""
	dimension = 1
	integer = 1
	prime_count = 0
	composite_count = 1
	not_found = True
	while not_found:
		# the increment to keep a perfect square must be 2
		dimension += 2
		# the step distance from 1 corner to the next between corners, works fine from one level to the next one up
		step = dimension - 1
		# one for each corner
		for _ in range(4):
			integer += step
			# determine primality of corner integer
			if isPrime(integer):
				prime_count += 1
			else:
				composite_count += 1
		# now before we increase the spiral iteration test the ratio
		if prime_count / (prime_count + composite_count) < percentage/100:
			not_found = False
	return dimension


if __name__ == "__main__":
	ans = spiral_matrix(10)
	print("The width of the square spiral where the ratio of primes along both diagonals first falls below 10% is:", ans)
