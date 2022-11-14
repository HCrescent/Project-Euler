"""Project Euler Problem 51 - Prime digit replacements"""


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


def findPrimeSet(set_size):
	""" Finds a set of prime numbers that are related by the digits replaced to generate them.

	:param set_size: Int - the size of the set we want to find
	:return: List - list of prime numbers
	"""
	# for each prime above single digit primes
	for each in prime_list[4:]:
		prime = list(str(each))
		prime_width = len(prime)  # prime width of digits for selecting the proper replacement masks
		# for each mask in the list for that prime width
		for mask in magnitude_masks[prime_width]:
			# per mask iteration we need a set of numbers that will contain all created integers
			mask_replacement_numbers = []
			# check the first and last bits of the mask to determine which replacement digits to use
			digit_case = mask[0] + mask[-1]
			match digit_case:
				case '00':
					# use all 10 digits
					replacement_list = middle_digits
				case '01' | '11':
					# because primes can only end in 1, 3, 7, 9
					replacement_list = least_significant_digits
				case '10':
					# exclude 0 for leading 0
					replacement_list = most_significant_digits
			# start the process of replacing digits based on the mask
			iteration_prime = prime.copy()  # we need a copy of list otherwise we will be editing the original
			# for each replacement digit, replace only the digits indicated by the mask
			# noinspection PyUnboundLocalVariable
			for replacement_digit in replacement_list:
				for i, status in enumerate(mask):
					if status == "1":
						iteration_prime[i] = replacement_digit
				mask_replacement_numbers.append(int("".join(iteration_prime)))
			# narrow list down by only members in the prime set
			mask_replacement_primes = [_ for _ in mask_replacement_numbers if _ in prime_set]
			# if we found it we can stop processing and return
			if len(mask_replacement_primes) == set_size:
				return mask_replacement_primes
	return []  # we shouldn't reach here but just in case well return an empty list instead of None type


if __name__ == "__main__":
	# initializations for crunching
	magnitude = 6
	target_set_size = 8
	prime_list = sieveEratosthenes(10**magnitude)
	prime_set = set(prime_list)
	least_significant_digits = ["1", "3", "7", "9"]
	most_significant_digits = [str(_) for _ in range(1, 10)]
	middle_digits = [str(_) for _ in range(10)]
	# replacement masks
	magnitude_masks = [[] for _ in range(magnitude + 1)]
	for tmp_magnitude in range(magnitude+1):
		for number in range(2**tmp_magnitude)[1:-1]:  # slicing excludes all 0's and all 1's
			# keep leading zeros for case matching and mask processing
			magnitude_masks[tmp_magnitude].append(str(bin(number))[2:].zfill(tmp_magnitude))
	# main crunch section
	found_primes = findPrimeSet(target_set_size)
	print("The smallest prime found such that by replacing digits makes an 8 member set of primes is:", found_primes[0])
