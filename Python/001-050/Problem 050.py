"""Project Euler Problem 50 - Consecutive prime sum"""
import time
start = time.time()


def sieveEratosthenes(n):
	""" Generates a list of prime numbers up to inclusive n

	:param n: Int - the upper bound of primes we want
	:return: List - list of prime numbers up to n inclusive
	"""
	# initialize the array for sieving, +1 to keep n included
	numbers = [True for _ in range(n+1)]
	# for 2 through floor of sqrt(n)
	for i in range(2, int(n**.5)+1):
		# if marked True its our next prime
		if numbers[i]:
			# starting at prime squared, run through all multiples marking its composites false
			sub_run = i**2
			# make sure <= to allow n to be flagged appropriately
			while sub_run <= n:
				numbers[sub_run] = False
				sub_run += i
	# list comprehension to convert the boolean array into the meaningful information
	prime_array = [index for index, status in enumerate(numbers) if status]
	# skip 0 and 1 when returning the list
	return prime_array[2:]


def slidingWindowSums(the_list, the_width):
	""" Takes a list and processes the sum of a sliding window section for the given list
	results are returned in a list format, where the index of the list matches
	the index starting point of the sliding window

	:param the_list: List - The list we want to analyze windows out of
	:param the_width: Int - The width of our sliding window
	:return: List - A list of corresponding window sums where the index is the starting position of the window
	"""
	window_sums = []
	# adjusted range based on window width
	for index in range(len(the_list) - (the_width - 1)):
		accumulator = 0
		# for each number in the window
		for num in the_list[index:index+the_width]:
			accumulator += num
		window_sums.append(accumulator)
	return window_sums


if __name__ == "__main__":
	prime_list = sieveEratosthenes(100_000)
	prime_set = set(prime_list)
	print(prime_set)
	print(prime_list)
	highest_width = 1
	highest_prime = 0
	starting_index = 0
	for width in range(21, len(prime_list)+1):
		sums_list = slidingWindowSums(prime_list, width)
		for summation in sums_list:
			if summation in prime_set:
				highest_width = width
				highest_prime = summation
				break
	print("highest_prime", highest_prime)
	print("highest_width", highest_width)
	end = time.time()
	total_time = end - start
	print("\n" + str(total_time))
