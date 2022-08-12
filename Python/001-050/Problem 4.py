"""Project Euler Problem 4 - Largest palindrome product"""


def isPalindrome(number):
	""" Determine if a given integer is a Palindrome (does not change when written backwards)

	:param number: Int - the number we want to check
	:return: Bool - Truthiness of palindrome status
	"""
	forwards_string = str(number)
	backwards_string = str(number)[::-1]

	return forwards_string == backwards_string


def findLargestPalindrome():
	""" creates a dictionary of palindromes made by a product of 3 digit integers

	:return: Str - function string of max palindrome value and its key product
	"""
	palindromes = {}
	for i in range(1000)[:100:-1]:
		for n in range(1000)[:100:-1]:
			if isPalindrome(i * n):
				palindromes.update({f"{i} x {n}": i * n})
	# this return function is finding the dict key by largest palindrome and then the also its value in a string
	return f"{max(palindromes, key=palindromes.get)} = {palindromes.get(max(palindromes, key=palindromes.get))}"


if __name__ == "__main__":
	print("The largest palindrome of a product of two three-digit numbers is: ", findLargestPalindrome())
