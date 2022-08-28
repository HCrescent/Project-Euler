"""Project Euler Problem 16 - Power digit sum"""
# I think when I try to calculate 2^1000 in python it will just do it for me but if this was me doing it 20 years ago
# I would have to take the same thought solution to large sum, but instead of 100 50 digit numbers adding together
# I would use the same function for a large sum, but with splitting the exponent into several smaller powers of 2
# basically would have to reduce it to a list of integers of powers of two below 2^32 so the cpu could calculate
# those then split them into arrays of single digits to add together the same way you would on paper


if __name__ == "__main__":
	x = sum(list(map(int, str(2**1000))))
	print(x)
