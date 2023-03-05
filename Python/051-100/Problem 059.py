"""Project Euler Problem 59 - XOR decryption"""
with open("text inputs/Problem 059.txt", 'r') as infile:
	data = [int(each) for each in infile.readline().split(',')]
lowercase = 97, 122
uppercase = 65, 90
message_range = 32, 126


def read(ascii_codes):
	# prints out the ascii codes to the screen as text
	decrypted = "".join([chr(each) for each in ascii_codes])
	print(decrypted)
	pass


def probablyReadable(ascii_nums):
	# determines via custom heuristic if the message is decrypted (not infallible)
	total_chars = len(ascii_nums)
	valid_ascii = 0
	# we are going to assume that the message is probably readable if 90% of the characters are in this range
	for ascii_val in ascii_nums:
		if lowercase[0] <= ascii_val <= lowercase[1] or uppercase[0] <= ascii_val <= uppercase[1]:
			valid_ascii += 1
	# i manually narrowed this scope down until it gave the correct results, need to automate that narrowing down
	if valid_ascii/total_chars >= .735:
		return True
	else:
		return False


def keyCycle(word):
	""" simple function that continuously yields the next character of a cipher key

	:param word: List - list of ascii values for the cipher key
	:return:
	"""
	while True:
		for each in word:
			yield each


def decrypt():
	keys = generateKeys()
	message = data.copy()
	while not probablyReadable(message):
		message = data.copy()
		key_cycle = keyCycle(next(keys))
		for i, char in enumerate(message):
			message[i] = char ^ next(key_cycle)
	read(message)
	print(sum(message))
	return


# learn yields!!!!!!!!
def generateKeys():
	for p0 in range(97, 123):
		for p1 in range(97, 123):
			for p2 in range(97, 123):
				yield [p0, p1, p2]


if __name__ == "__main__":
	decrypt()
