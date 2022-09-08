"""Project Euler Problem 22 - Names scores"""
with open("text inputs/Problem 022.txt", 'r') as infile:
	# formatting the data with a single line list comprehension
	names = [_.strip("\"") for _ in infile.read().split(",")]
	names.sort()
	keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	letter_scores = {each: i+1 for (i, each) in enumerate(keys)}


def scoreNames(name_list):
	""" Creates a list of scored names with the scoring rules dictated by the problem question:
	each word is scored by the integer conversions of its letters, multiplied by its placement in
	alphabetical order
	:param name_list: List - ordered list of names
	:return: List - ordered list of name scores
	"""
	score_list = []
	for i, word in enumerate(name_list):
		score = 0
		for each in word:
			score += letter_scores[each]
		# multiply the score by its placement in the ordered list
		score *= i+1
		score_list.append(score)
	return score_list


if __name__ == "__main__":
	print("The total of all the name scores in the file is:", sum(scoreNames(names)))
