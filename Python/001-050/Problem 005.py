"""Project Euler Problem 5 - Smallest multiple"""


def calculate():
	""" Finds the smallest positive integer that is evenly divisible by all numbers 1 - 20

	:return: Int - our solution
	"""
	# math shortcuts, if these numbers pass all 1-20 passes.
	check_set = [11, 12, 13, 14, 15, 16, 17, 18, 19]
	accumulator = 0
	# loop until we find an answer
	while True:
		flag = True
		accumulator += 20
		for each in check_set:
			# if not evenly divisible set flag to False and break loop
			if accumulator % each != 0:
				flag = False
				break
		# if flag is still True at this point we found our answer
		if flag:
			return accumulator


if __name__ == "__main__":
	print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is: ", calculate())
