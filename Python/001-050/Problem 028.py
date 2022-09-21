"""Project Euler Problem 28 - Number spiral diagonals"""


def spiral_matrix_sum(size):
	""" calculates the sum of the diagonals of a matrix where starting with 1 in the center
	and incrementing in a clockwise spiral.

	:param size: int - dimensions of the square matrix, must be a multiple of 2 plus 1 so that there is a center origin
	:return: int - the accumulated sum of the diagonals of the matrix
	"""
	dimension = 1
	integer = 1
	accumulate = 1
	while dimension < size:
		# the increment to keep a perfect square must be 2
		dimension += 2
		# the step distance from 1 corner to the next between corners, works fine from one level to the next one up
		step = dimension - 1
		# one for each corner
		for _ in range(4):
			integer += step
			accumulate += integer
	return accumulate


if __name__ == "__main__":
	print("The sum of the numbers on the diagonals in a 1001 by 1001 spiral matrix is:", spiral_matrix_sum(1001))
