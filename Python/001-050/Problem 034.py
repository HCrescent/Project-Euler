"""Project Euler Problem 34 - Digit factorials"""
if __name__ == "__main__":
	factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
	special_nums = []
	# the upper bound will be no larger than 7 digits because 8 single digit factorials will never sum to 8 digits
	for n in range(3, factorial[9]*7):
		# list comprehension to take a string of a number, and int and factorial the digit
		if sum([factorial[int(_)] for _ in str(n)]) == n:
			special_nums.append(n)
	print("The sum of all numbers which are equal to the sum of the factorial of their digits:", sum(special_nums))
