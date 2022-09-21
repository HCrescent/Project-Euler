"""Project Euler Problem 27 - Quadratic primes"""


def quadratic_form(n, a, b):
	""" provides the output for quadratic formula form n^2 + an + b

	:param n: int - our whole number variable input
	:param a: int - a coefficient
	:param b: int - b coefficient
	:return: int - f(n)
	"""
	return n**2 + a*n + b


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


if __name__ == "__main__":
	b_coefficient = []
	coefficient_list = []
	prime_outputs = []
	# build prime b coefficients (for any n = 0, f(n) being a prime must have a b coefficient that's prime
	for each in range(1001):
		if isPrime(each):
			b_coefficient.append(each)
	# main driving code
	for B in b_coefficient:
		for A in range(-1000, 1001):
			N = 0
			# while input results in a prime output, increment input
			while isPrime(quadratic_form(N, A, B)):
				N += 1
			if N > 1:
				coefficient_list.append([A, B])
				prime_outputs.append(N)
	# get the index of the largest consecutive prime outputs to match with the stored coefficients
	index = prime_outputs.index(max(prime_outputs))
	print(f"Quadratic formula for {prime_outputs[index]} consecutive primes")
	print(f"n^2 + {coefficient_list[index][0]}n + {coefficient_list[index][1]}")
	print("The product of the coefficients is:", coefficient_list[index][0] * coefficient_list[index][1])
