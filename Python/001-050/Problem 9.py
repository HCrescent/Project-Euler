"""Project Euler Problem 9 - Special Pythagorean triplet"""
# a < b < c
# a**2 + b**2 = c**2
# a + b + c = 1000
# 1000 = sqrt(a**2 + b**2) + a + b, a < b


def find_abc():
	""" Finds the only Pythagorean Triplet where a+b+c=1000 a<b<c

	:return: int int int - our calculated A B and C
	"""
	for a in range(501)[1::]:
		for b in range(501)[a+1::]:
			# this equation is derived from rewriting our two equations to equate c in terms of a and b
			# and then removing c as a variable by substitution for an easier 2 variable equation.
			if ((a**2 + b**2)**.5 + a + b) == 1000:
				return a, b, 1000 - a - b


if __name__ == "__main__":
	A, B, C = find_abc()
	print("Pythagorean triplet for which a + b + c = 1000 is: ", A, B, C)
	print("The product abc is: ", A*B*C)
