"""Project Euler Problem 34 - Digit factorials"""
import time
start = time.time()


def factorial(number):
	""" simple factorial function, can also use import math for math.factorial() for a faster built in function

	:param number: Int - the number we want to calculate the factorial of
	:return: Int - the final product
	"""
	product = 1
	for each in range(1, number+1):
		product *= each
	return product


if __name__ == "__main__":
	special_nums = []
	# the upper bound will be no larger than 7 digits because 8 single digit factorials will never sum to 8 digits
	for n in range(3, factorial(9)*7):
		# list comprehension to take a string of a number, and int and factorial the digit
		if sum([factorial(int(_)) for _ in str(n)]) == n:
			special_nums.append(n)
	print("The sum of all numbers which are equal to the sum of the factorial of their digits:", sum(special_nums))
	end = time.time()
	total_time = end - start
	print("\n" + str(total_time))
