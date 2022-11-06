"""Project Euler Problem 48 - Self powers"""


def truncateLeft(value, digits):
	return value - (value // 10**digits) * 10**digits


if __name__ == "__main__":
	total = 0
	for each in range(1, 1001):
		total += each**each
	print("The last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000:", truncateLeft(total, 10))
