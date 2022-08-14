"""Project Euler Problem 7 - 10001st prime"""
import time
start = time.time()


def factorize(value):
	"""Determines if given value is prime or not

	:param value: int - number we are going to factorize
	:return: Bool - Truthiness of prime status
	"""

	searching = True
	prime = False
	# run until our first prime factor is found
	while searching:
		# for loop until you hit the first possible divisor, guaranteed to be prime
		# starts at 3 because 1 is not prime and we are skipping 2 as the only even prime
		# ends at value (if largest factor is itself), only check odd numbers to save time
		for number in range(3, value + 1, 2):
			# if number divides evenly check if our first prime is itself of not
			if value % number == 0:
				if number < value:
					searching = False
					break
				prime = True
				searching = False
	return prime


def countPrimes(number):
	accumulator = 1
	primesFound = 1  # start at 1 because we will never calculate the first prime of 2
	while primesFound < number:
		accumulator += 2  # skip even numbers
		if factorize(accumulator):
			primesFound += 1
	return accumulator


if __name__ == "__main__":
	print(countPrimes(10001))
	end = time.time()
	total_time = end - start
	print("\n" + str(total_time))
