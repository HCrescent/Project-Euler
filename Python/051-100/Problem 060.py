"""Project Euler Problem 60 - Prime pair sets"""
# quick abstract, find the smallest sum of a set of 5 primes, where every permutation of 5 choose 2 results in a prime


def bad_approach(ones):
	count = 0
	control = []
	while count < 1000:
		if bin(count).count('1') == ones:
			print(bin(count)[2:])
			control.append(bin(count)[2:])
		count += 1
	return control


def fast_approach(ones):
	base_bin = ['1' for _ in range(ones)]
	yield "".join(base_bin)  # always offer the starting mask
	zero_count = 1
	while True:
		zero_list = ['0' for _ in range(zero_count)]  # for testing equality
		new_base = base_bin.copy()
		[new_base.insert(1, '0') for _ in range(zero_count)]  # insert the zeros
		yield "".join(new_base)  # give the first iteration before swapping
		while new_base[-zero_count:] != zero_list:  # while the last digits are not all the zeros
			# start swapping at the rightmost zero to the end of list
			for i in range(zero_count, len(new_base)-1):
				new_base[i], new_base[i+1] = new_base[i+1], new_base[i]
				yield "".join(new_base)
		# after we reached the end of that magnitudes permuations we can increase the zero width by one
		zero_count += 1


if __name__ == "__main__":
	control_bin = bad_approach(4)
	print(control_bin)
	masks = fast_approach(4)
	while True:
		input()
		print(next(masks))
