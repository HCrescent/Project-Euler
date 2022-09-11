"""Project Euler Problem 20 - Factorial digit sum"""


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
	print("The sum of the digits in the number 100! is", sum(list(map(int, str(factorial(100))))))
