"""Project Euler Problem 40 - Champernowne's constant"""
if __name__ == "__main__":
	constant = ""
	number = 0
	width = 0
	# construct a string of the constant
	while width <= 1_000_000:
		temp_str = str(number)
		constant = constant + temp_str
		width += len(temp_str)
		number += 1
	# extract the request digits and product them
	total = 1
	for magnitude in range(7):
		total *= int(constant[10**magnitude])
	print("d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000 of Champernowne's constant:", total)
