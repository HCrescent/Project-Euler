"""Project Euler Problem 6 - Sum square difference"""


def sum_of_squares(number):
	""" Calculates the sum of squares of all natural numbers in a given range

	:param number: Int - our summation range bound
	:return: Int - finished summation of squares
	"""
	summation = 0
	for each in range(1, number+1):
		summation += each**2
	return summation


def square_of_sum(number):
	""" Calculates the square of the summation of all natural numbers in a given range

	:param number: Int - our summation range bound
	:return: Int - finished square of the summation
	"""
	summation = 0
	for each in range(1, number+1):
		summation += each
	return summation**2


if __name__ == "__main__":
	sum1 = sum_of_squares(100)
	sum2 = square_of_sum(100)
	print("sum of squares: ", sum1)
	print("square of sum: ", sum2)
	print(
		"The difference between the sum of the squares of the first one hundred natural numbers and the square of "
		"the sum is: ", sum2 - sum1
	)
