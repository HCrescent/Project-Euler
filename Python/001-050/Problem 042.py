"""Project Euler Problem 42 - Coded triangle numbers"""
with open("text inputs/Problem 042.txt", 'r') as infile:
	# formatting the data with a single line list comprehension
	words = [_.strip("\"") for _ in infile.read().split(",")]
keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letter_scores = {each: i+1 for (i, each) in enumerate(keys)}


def triangleNumber(n):
	""" returns nth triangle number using formula n(n+1)/2

	:param n: Int - number 'n'
	:return: Int - triangle number
	"""
	return n*(n+1)//2


def scoreWords(words_list):
	""" Creates a list of scored names with the scoring rules dictated by the problem question:
	each word is scored by the sum of integer conversions of its letters
	:param words_list: List - list of words
	:return: List - list of word scores
	"""
	score_list = []
	for word in words_list:
		score = 0
		for letter in word:
			score += letter_scores[letter]
		score_list.append(score)
	return score_list


if __name__ == "__main__":
	triangle_numbers = {triangleNumber(_) for _ in range(1, 1000)}
	scores_list = scoreWords(words)
	triangle_count = 0
	for each in scores_list:
		if each in triangle_numbers:
			triangle_count += 1
	print("The number of words in the text file that translate into triangle numbers:", triangle_count)
