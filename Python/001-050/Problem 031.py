"""Project Euler Problem 31 - Coin sums"""


def unique_denomination_sums(denominations, total, current_smallest, count=0):
	""" counts how many ways you can make change for SMALL totals of cash (given in smallest units)

	:param denominations: list - coin
	:param total:
	:param current_smallest:
	:param count:
	:return:
	"""
	# terminating section
	# if total is less the the second smallest denomination
	if total < denominations[1]:
		# if total is already zero we are done
		if total == 0:
			count += 1
		# else if total mod the smallest denomination is zero that means the rest of it fits into our smallest size
		elif total % denominations[0] == 0:
			count += 1
		return count
	# main section
	# for each in the reverse sorted denominations
	for each in denominations[::-1]:
		# total cash left is greater or equal to each, and is smaller or equal to the smallest denomination used
		if total >= each and each <= current_smallest:
			# if our current denomination isn't 1,
			if each != 1:
				new_total = total - each
			# if we are on our smallest denomination
			elif each == denominations[0] and total % each == 0:
				new_total = 0
			else:
				new_total = total
			current_smallest = each
			count = unique_denomination_sums(denominations, new_total, current_smallest, count)
	return count


if __name__ == "__main__":
	coins = [3, 7, 25, 50]

	print(unique_denomination_sums(coins, 200, coins[-1]))

