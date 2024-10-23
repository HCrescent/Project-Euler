"""Project Euler Problem 63 - Powerful Digit Counts"""
from math import log10, ceil

def exploreExponents():
	count = 0
	# the arbitrary upper bound because obviously
	for exponent in range(1, 100):
		for number in range(1, 100):
			powered = number ** exponent
			#ignore 10 to any power because the log test provides an integer that cant be round up for digit count
			if (ceil(log10(powered)) == exponent) and (powered % 10 != 0):
				# print(f"number: {number}\t\texponent: {exponent}\t\tpowered: {powered}")
				count += 1
	return count+1 # +1 for 1^1 which log test cant catch because log100(1) = 0

if __name__ == "__main__":
	print("How many n-digit positive integers exist which are also an n'th power?: ", exploreExponents())
