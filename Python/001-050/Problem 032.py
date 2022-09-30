"""Project Euler Problem 32 - Pandigital products"""
if __name__ == "__main__":
	product_list = []
	temp = [str(_) for _ in range(1, 10)]
	pandigital_set = set(temp)
	# 5000 was chosen because 2 times a 4 digit number, that results in a 4 digit number
	# can lead to a 9 digit concatenation, while 2 times 5000+ cannot result in a 4 digit number
	for multiplicand in range(1, 5000):
		for multiplier in range(1, 5000):
			product_identity = multiplicand * multiplier
			# create a string of all the digits
			concat = str(multiplicand) + str(multiplier) + str(product_identity)
			# if the length of the concatenation is the same as the length of our set we can check if its equal
			if len(concat) == len(pandigital_set):
				if set(concat) == pandigital_set:
					product_list.append(product_identity)
	product_list = list(set(product_list))  # remove duplicates
	ans = sum(product_list)
	print("Sum of all products whose multiplicand/multiplier/product identity can be written as a 1-9 pandigital:", ans)
