"""Project Euler Problem 31 - Coin sums"""


def unique_denomination_sums(denominations, total, current_smallest, count=0):
	""" counts how many ways you can make change for small totals of cash (given in smallest units)

	:param denominations:
	:param total:
	:param current_smallest:
	:param count:
	:return:
	"""
	# terminating section
	# if total is less the the second smallest denomination
	if total < denominations[1]:
		if total == 0:
			count += 1
		elif total % denominations[0] == 0:
			count += 1
		return count
	# main section
	for each in denominations[::-1]:
		if total >= each and each <= current_smallest:
			if each != 1:
				new_total = total - each
			else:
				new_total = 0
			current_smallest = each
			count = unique_denomination_sums(denominations, new_total, current_smallest, count)
	return count


if __name__ == "__main__":
	coins = [1, 2, 5, 10, 20, 50, 100, 200]

	print(unique_denomination_sums(coins, 200, coins[-1]))

