"""Project Euler Problem 31 - Coin sums"""
# poor solution, too slow for large totals, solves the requested answer but I want a universally usable version


def unique_denomination_sums(denominations, total, current_smallest, count=0):
	""" counts how many ways you can make change for SMALL totals of cash (given in smallest units)

	:param denominations: list - coin
	:param total: int - the total of cash (in smallest units, to be divided into partitions
	:param current_smallest: int - the smallest denomination the current recursion level should consider
	:param count: int - total number of unique arrangements of denominations totaling
	:return: int - total number of unique arrangements of denominations totaling
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
			# if our denomination is unitary (1), new total is zero
			else:
				new_total = 0
			# prevent returning to a larger denomination on the next recursion level deeper
			current_smallest = each
			count = unique_denomination_sums(denominations, new_total, current_smallest, count)
	return count


if __name__ == "__main__":
	coins = [1, 2, 5, 10, 20, 50, 100, 200]
	print("The number of ways can £2 be made using any number of coins:", unique_denomination_sums(coins, 200, coins[-1]))
