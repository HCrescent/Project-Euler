"""Project Euler Problem 31 - Coin sums"""


def unique_denomination_sums(denominations, total, count=0):
	""" counts how many ways you can make change for small totals of cash (given in smallest units)

	:param denominations: list - the available coin denominations, pass in descending order
	:param total: int - the total number we want to find unique partitions of
	:param count: int -
	:return: int -
	"""
	# terminating section
	if total == 0:
		count += 1
		return count
	# main section
	while total > 0:
		for each in denominations:
			if total >= each:
				new_total = total - each
				count = unique_denomination_sums(denominations, new_total, count)
	return count


if __name__ == "__main__":
	coins = [1, 5, 10, 25, 50]

	print(unique_denomination_sums(coins[::-1], 50))

