"""Project Euler Problem 18 - Maximum path sum I"""
with open("text inputs/Problem 018.txt", 'r') as infile:
	# one liner formatting: for each line in the infile, map the integer function on to each string split by a space
	matrix_map = [list(map(int, line.split(' '))) for line in infile]


def backwardsPath(pyramid):
	""" Finds the largest sum path through a triangle arrangement of integers as given in the problem

	:param pyramid: List - a list of lists made from the text of the numeric pyramid
	:return: Int - the largest sum possible through the pyramid
	"""
	# start on the second to last row
	row = len(pyramid) - 2
	# while we are not out of range of the top of the pyramid
	while row >= 0:
		# for each index of the current row
		for i in range(len(pyramid[row])):
			# if the left sub-term is greater than the right sub-term
			if pyramid[row+1][i] > pyramid[row+1][i+1]:
				# add left sub-term to our current term
				pyramid[row][i] += pyramid[row+1][i]
			# else if right sub-term is greater or equal
			else:
				# add right sub-term to our current term
				pyramid[row][i] += pyramid[row+1][i+1]
		row -= 1
	return pyramid[0][0]


if __name__ == "__main__":
	print("The maximum sum from top to bottom of the given triangle is:", backwardsPath(matrix_map))
