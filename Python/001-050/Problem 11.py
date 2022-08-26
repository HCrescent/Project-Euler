"""Project Euler Problem 11 - Largest product in a grid"""
with open("text inputs/Problem 11.txt", 'r') as infile:
	# one liner formatting: for each line in the infile, map the integer function on to each string split by a space
	matrix_map = [list(map(int, line.split(' '))) for line in infile]


def windowProduct(matrix):
	""" simple window product slider for a static sized input

	:param matrix: List of Lists - a 2D array from our input
	:return: Int - the largest product
	"""
	products = []
	# range limits to prevent accessing elements outside of bounds
	for x in range(17):
		for y in range(17):
			# flat horizontal line
			products.append(matrix[x][y] * matrix[x][y+1] * matrix[x][y+2] * matrix[x][y+3])
			# positive diagonal line
			products.append(matrix[x][y] * matrix[x+1][y+1] * matrix[x+2][y+2] * matrix[x+3][y+3])
			# vertical line
			products.append(matrix[x][y] * matrix[x+1][y] * matrix[x+2][y] * matrix[x+3][y])
			if x > 2:
				# negative diagonal line
				products.append(matrix[x][y] * matrix[x-1][y+1] * matrix[x-2][y+2] * matrix[x-3][y+3])
	return max(products)


if __name__ == "__main__":
	print("The greatest product of four adjacent numbers in the same direction is: ", windowProduct(matrix_map))
