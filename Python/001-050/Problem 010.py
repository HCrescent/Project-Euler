"""Project Euler Problem 10 - Summation of primes"""


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


def sumPrimes(number):
	""" Calculates the summation of all prime numbers below a given bound

	:param number: Int - the upper bound for our summation
	:return: - Int - the finished summation
	"""
	# summation starts at 2 because 2 is the only even prime and we will be skipping even numbers
	summation = 2
	accumulator = 3
	while accumulator < number:
		if isPrime(accumulator):
			summation += accumulator
		accumulator += 2  # skip even numbers
	return summation


if __name__ == "__main__":
	print("The sum of all prime numbers below 2 million is: ", sumPrimes(2000000))
