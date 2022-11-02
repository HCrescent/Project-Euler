"""Project Euler Problem 39 - Integer right triangles"""


def rightTriangleCompletion(a, b, c):
	""" Takes 2 sides of a right triangle and completes the third side, 0 denotes the unknown side length

	:param a: Int - length of side a
	:param b: Int - length of side b
	:param c: Int - length of hypotenuse
	:return: List - all three sides of the completed triangle
	"""
	try:
		assert (a, b, c).count(0) == 1
	except AssertionError:
		raise AssertionError(f"Input Must contain only 1 unknown side length for (a, b, c), input: ({a}, {b}, {c})")
	n = [a, b, c].index(0)
	match n:
		case 0:
			a = (c**2-b**2)**.5
		case 1:
			b = (c**2-a**2)**.5
		case 2:
			c = (a**2+b**2)**.5
	return [a, b, c]


if __name__ == "__main__":
	limit = 1000
	# 2x is breathing room for possible index locations which we don't know the exact highest
	perimeters = [set() for _ in range(2*limit)]
	# narrow the scope a bit since we know A + B + C has to be less than 1000
	for A in range(1, limit//2):
		for B in range(1, limit//2):
			# complete the triangle
			temp_triangle = rightTriangleCompletion(A, B, 0)
			# if C is an integer
			if temp_triangle[2].is_integer():
				# place the triangle in the index equal to its perimeter
				# using sets because we don't want to count swaps of A and B, only unique triangles
				# frozen set because you cant have a set of sets as sets themselves are not hashable
				perimeters[int(sum(temp_triangle))].add(frozenset(temp_triangle))
	# create an array where the index as a perimeter has the number of unique unit triangles
	winners = [len(perimeters[i]) for i in range(limit+1)]
	# find the maximum and its perimeter
	winning_perimeter = winners.index(max(winners))
	print("The value of p ≤ 1000 for which the number of solutions is maximised:", winning_perimeter)
