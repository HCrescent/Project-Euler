"""Project Euler Problem 7 - 10001st prime"""


def isPrime(value):
	""" Determines if a number is prime, for efficiency sake we are only testing values greater than 2
	to avoid edge cases 1 being not prime and 2 being prime

	:param value: Int - Number to check if prime
	:return: Bool - Our truthiness value of prime status
	"""
	# our upper range bound is the square root rounded plus 1 to offset the exclusive end of range function
	# the reason for the square root is a shortcut, a whole number factor will never be more than the square root.
	# then for extra efficiency we increment by two to avoid checking even value which will never be a factor of odd#
	for each in range(3, int(value ** .5)+1, 2):
		# if value mod each is zero we found a factor too early and we know its not prime
		if value % each == 0:
			return False
	# reaching this line means we never found a factor and its Prime
	return True


def countPrimes(number):
	""" Finds the enumerated prime number excluding edge case 2 which is accounted for in the calculation

	:param number: Int - the enumeration of the prime we wish to find
	:return: - Int - the desired calculated prime number called for by the function
	"""
	accumulator = 1
	primesFound = 1  # start at 1 because we will never calculate the first prime of 2
	while primesFound < number:
		accumulator += 2  # skip even numbers
		if isPrime(accumulator):
			primesFound += 1
	return accumulator


if __name__ == "__main__":
	print("The 10,001st Prime number is: ", countPrimes(10001))
