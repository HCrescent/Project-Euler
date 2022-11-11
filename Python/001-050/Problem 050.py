"""Project Euler Problem 50 - Consecutive prime sum"""


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


if __name__ == "__main__":
	prime_list = sieveEratosthenes(1_000_000)
	prime_set = set(prime_list)
	highest_width = 1
	highest_prime = 0
	last_sum = 0
	# to narrow our scope we will start with a simple sum starting from the first prime
	# it wont be guaranteed to be the highest prime constructable
	# while our sum is less than the largest prime in our prime_list
	while last_sum < prime_list[-1]:
		for i in range(len(prime_list)):
			# rolling sum of primes starting from position 0
			last_sum += prime_list[i]
			# at each step check if we hit a prime number
			if last_sum in prime_set:
				# set the flags to the most recent info found
				highest_width = i+1
				highest_prime = last_sum
	# now we know that the highest prime that can be the sum of the most consecutive primes is at LEAST highest_prime
	# and the width of consecutive primes is at LEAST highest_width
	master_sum = highest_prime
	# while our scope of width can be less than the largest prime
	while master_sum < prime_list[-1]:
		iteration_sum = master_sum
		# create temporary wave two list
		wave_two_list = []
		# for the length of the prime list, slide the window sum
		for i in range(len(prime_list)):
			# adding the next element in prime_list then removing the first element of our window
			iteration_sum += prime_list[highest_width + i]
			iteration_sum -= prime_list[i]
			# only slide as long as our window sum is less than the largest prime
			if iteration_sum < prime_list[-1]:
				# check the sum as a key in prime set
				if iteration_sum in prime_set:
					wave_two_list.append(iteration_sum)
			# this clause will break the for loop as we don't want to process past consecutive sums
			# that will result in a number higher than our largest prime
			else:
				break
		# if we found a sum that was a prime our highest prime will be the last element in the list
		if len(wave_two_list) > 0:
			highest_prime = wave_two_list[-1]
			# new_highest_width = highest_width  # if you want to know how many terms uncomment and print this at end
		# add the next prime to the master sum as our indicator for the sum of our smallest window sum
		master_sum += prime_list[highest_width]
		# increase the window width by 1
		highest_width += 1
	print("Which prime, below one-million, can be written as the sum of the most consecutive primes:", highest_prime)
