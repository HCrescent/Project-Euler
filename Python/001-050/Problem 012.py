"""Project Euler Problem 12 - Highly divisible triangular number"""


def triangleNumber(n):
	""" returns nth triangle number using formula n(n+1)/2

	:param n: Int - number 'n'
	:return: Int - triangle number
	"""
	return int(n*(n+1)/2)


def primeFactorize(value):
	"""Returns a list of prime factors of given whole number.

	:param value: int - number we are going to factorize
	:return: list - list of prime factors
	"""
	# always check 2 first
	number = 2
	prime_factors = []
	# run until our value is reduced to 1
	while value > 1:
		# always start from the largest prime factor found last
		if len(prime_factors) > 0:
			number = prime_factors[-1]
		# while loop until you hit the first possible divisor, guaranteed to be prime
		# starts at 2 because 1 is not prime and always divisible
		# ends at value/2 (if largest factor is itself)
		while number < value/2:
			# if number divides evenly
			if value % number == 0:
				# use floored division to prevent expanding int to float
				value //= number
				# append prime factor to list
				prime_factors.append(number)
				# breaks after first prime factor
				break
			# this check is so we can include prime number 2 in our factor checks
			# if LSB of number is 1 we are odd and can skip all the rest of even numbers
			# else move from 2 -> 3
			if number & 1:
				number += 2
			else:
				number += 1
		# since we stopped early to save checking obviously wrong factors
		if number > value/2:
			# at this point there are no more factors than our leftover value itself
			prime_factors.append(value)
			# lowering value to 1 to prepare to exit function
			value /= value
	return prime_factors


def totalFactors(number):
	""" Taking a list of prime factors calculate the total number of factors derived from a formula
		of (a+1)(b+1)(c+1)... where the variables are the power of each prime factor

	:param number: Int - triangle number of which we want to know how many factors exist
	:return: Int - the total number of factors
	"""
	total_factors = 1
	prime_factors = primeFactorize(number)
	for each in set(prime_factors):
		total_factors *= (prime_factors.count(each) + 1)
	return total_factors


def findXFactors(bound):
	""" Finds N where Nth triangle number is the first triangle number with over 'bound' factors

	:param bound: Int - the lower bound for how many factors we want to find
	:return: Int - the correct N for Nth triangle number with more than 'bound' factors
	"""
	N = 0
	while totalFactors(triangleNumber(N)) < bound:
		N += 1
	return N


if __name__ == "__main__":
	Nth = findXFactors(500)
	print("The 1st Triangle number with more than 500 divisors: N =", Nth, "Triangle number: ", triangleNumber(Nth))
