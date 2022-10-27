"""Project Euler Problem 36 - Double-base palindromes"""


def isPalindrome(number):
	""" Determine if a given integer is a Palindrome (does not change when written backwards)

	:param number: Int - the number we want to check
	:return: Bool - Truthiness of palindrome status
	"""
	return str(number) == str(number)[::-1]


if __name__ == "__main__":
	base_10_palindromes = []
	for _ in range(1000000):
		if isPalindrome(_):
			base_10_palindromes.append(_)
	base_10_and_2_palindromes = []
	for each in base_10_palindromes:
		# exclude the 0b marker from the binary string
		if isPalindrome(str(bin(each))[2:]):
			base_10_and_2_palindromes.append(each)
	total = sum(base_10_and_2_palindromes)
	print("The sum of all numbers, less than one million, which are palindromic in base 10 and base 2", total)
