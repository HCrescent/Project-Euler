"""Project Euler Problem 12 - Large sum"""
# this problem is trivial in python but if I had to do it with restricted integer sizes
# i would split each large integer into an array of single digit integers
# and then from right to left sum all the single digits in that power of 10
# and append carry's to the proper digits and then at the end concatenate the resulting list
# for the first ten digits
with open("text inputs/Problem 013.txt", 'r') as infile:
	data = [int(line.rstrip()) for line in infile]


if __name__ == "__main__":
	print("The first ten digits of the sum of the given large integers is: ", str(sum(data))[:10])
