"""Project Euler Problem 55 - Lychrel numbers"""


def isPalindrome(number):
	""" Determine if a given integer is a Palindrome (does not change when written backwards)

	:param number: Int - the number we want to check
	:return: Bool - Truthiness of palindrome status
	"""
	return str(number) == str(number)[::-1]


def searchLychrel(value, depth=0):
	""" Tries to find a palindrome by a specific method, with which not finding it denotes a Lychrel Number

	:param value: Int - the integer we will flip and add
	:param depth: Int - recursion depth counter
	:return: Bool - status of our starting number being a Lychrel Number
	"""
	# the depth limit of searching, if we hit this then there no palindrome (at least with reasonable computing power)
	# thus it is considered a Lychrel Number, we can exit the recursion
	if depth == depth_limit:
		return True
	# reverse the integer and add it to the original
	reverse_value = int(str(value)[::-1])
	new_value = value + reverse_value
	# if its a palindrome make our way out of the stack
	if isPalindrome(new_value):
		return False
	# the recursive call will bring our boolean value back up the stack
	return searchLychrel(new_value, depth+1)


if __name__ == "__main__":
	exclusive_bound = 10_000
	depth_limit = 50
	lychrel_numbers = [searchLychrel(N) for N in range(exclusive_bound)]
	total = lychrel_numbers.count(True)
	print("The number of Lychrel numbers are there below ten-thousand:", total)
