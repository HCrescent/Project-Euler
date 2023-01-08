"""Project Euler Problem 56 - Powerful digit sum"""


def powerfulDigits():
	totals = []
	for A in range(101):
		for B in range(101):
			# get the sum of the digits in the integer A**B
			totals.append(sum(map(int, str(A**B))))
	return max(totals)


if __name__ == "__main__":
	print("For natural numbers of the form, ab, where a, b < 100, the maximum digital sum is:", powerfulDigits())
