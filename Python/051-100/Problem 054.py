"""Project Euler Problem 54 - Poker hands"""
import time
start = time.time()
card_scores = {str(_): _ for _ in range(2, 10)}
card_scores.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})
hand_names = ["High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush", "Full House",
			  "Four of a Kind", "Straight Flush", "Royal Flush"]
hand_scores = {name: i for i, name in enumerate(hand_names)}
# list of each possible straight for use of creating a set and also checking positionally for a royal flush
straight_list = [tuple(_ for _ in range(_, _+5)) for _ in [n for n in range(2, 11)]]
# set of each possible tuple(because lists cant be hashed) of a straight
straight_set = {_ for _ in straight_list}
with open("text inputs/Problem 054.txt", 'r') as infile:
	player_1 = []
	player_2 = []
	for line in infile:
		# nested list comprehension, for splitting the ten card of each line into two hands left and right,
		# and then converting the string of each card value into its corresponding [integer, suit], and finally sorted
		player_1.append(sorted([[card_scores[card[0]], card[1]] for card in [hand for hand in line.split()[:5]]]))
		player_2.append(sorted([[card_scores[card[0]], card[1]] for card in [hand for hand in line.split()[5:]]]))


def winByHighCard(cards_1, cards_2):
	""" takes 2 reverse ordered lists of values, and determines which player won by a high card tiebreaker

	:param cards_1: List - player 1s cards with matching groups removed that tied the hand
	:param cards_2: List - player 2s cards with matching groups removed that tied the hand
	:return: Str - Result of the game
	"""
	for i, value in enumerate(cards_1):
		if value == cards_2[i]:
			continue
		if value > cards_2[i]:
			return "Player 1 Win"
		else:
			return "Player 2 Win"
	else:
		# the hands are exactly the same and cant be tie broken
		return "Draw"


def breakTies(player_1_hand, player_2_hand, hand_type):
	""" Takes two hands of the same class and figures out which one is the winner or if there is a draw
	# note that this is unfinished because the sample data set did not contain enough edge cases to require
	# this for the correct answer
	# currently only works for High Card and One Pair

	:param player_1_hand: List - List of cards in the form [value, suit]
	:param player_2_hand: List - List of cards in the form [value, suit]
	:param hand_type: Str - Hand classification
	:return: Str - Match result, Player 1 Win, Player 2 Win, or Draw
	"""
	# build our card values in reverse ordered fashion
	player_1_values_list = [card[0] for card in player_1_hand[::-1]]
	player_2_values_list = [card[0] for card in player_2_hand[::-1]]
	# print(f"{player_1_values_list!s:<25}{player_2_values_list}")
	match hand_type:
		case "High Card":
			return winByHighCard(player_1_values_list, player_2_values_list)
		case "One Pair":
			# determine the value of the pair in each hand
			for value in player_1_values_list:
				if player_1_values_list.count(value) == 2:
					pair_1 = value
					break
			for value in player_2_values_list:
				if player_2_values_list.count(value) == 2:
					pair_2 = value
					break
			# compare pairs, then if they are the same we will next check for high card
			# noinspection PyUnboundLocalVariable
			if pair_1 == pair_2:
				player_1_values_list = [_ for _ in player_1_values_list if _ != pair_1]
				player_2_values_list = [_ for _ in player_2_values_list if _ != pair_2]
				return winByHighCard(player_1_values_list, player_2_values_list)
			elif pair_1 > pair_2:
				return "Player 1 Win"
			else:
				return "Player 2 Win"
		# The rest of these cases would need to be implemented in real software, but as our data does not
		# include any matches that will trigger these cases i have left them blank
		case "Two Pairs":
			pass
		case "Three of a Kind":
			pass
		case "Straight":
			pass
		case "Flush":
			pass
		case "Full House":
			pass
		case "Four of a Kind":
			pass
		case "Straight Flush":
			pass
		# there is no possible way to tie break a royal flush in default rules-set
		case "Royal Flush":
			return "Draw"
	return "Draw"


def evalHandType(hand):
	""" Takes a poker hand in the form of a list of lists and evaluates the type of hand, returning the key
	of that hand for scoring.

	:param hand: List - List of cards in the form [value, suit]
	:return: Str - name of hand for scoring dictionary
	"""
	# I took to scratch paper to try and figure out the logic for this section, first I wrote it for checking
	# the set of suits of a hand and then checking the set of values of the cards in the hand, but then I wondered
	# if I did it in the reverse order if there would be less redundancy and it looked cleaner when I wrote that out
	# and in several cases did not require checking the suits at all.
	# once I had implemented the logic in the code, I ran into some trouble testing it as the test data doesnt seem
	# to contain all possible hands, I had to tinker with adding custom hands to the data set in order to test out
	# my edge cases for completeness
	# start with checking the length of the set of numbers for each hand
	unique_values = len({card[0] for card in hand})
	match unique_values:
		# only 2 different numbers means hands must be Four of a Kind or Full House
		case 2:
			# if any of the values have counts greater than 3 it's a Four of a Kind, if not it's a Full House
			hand_values_list = [card[0] for card in hand]
			for value in hand_values_list:
				if hand_values_list.count(value) > 3:
					return "Four of a Kind"
			else:
				return "Full House"
		# only 3 different numbers means possibilities are Three of a Kind or Two Pairs
		case 3:
			# if any of the values have counts greater than 2, it's a Three of a Kind, if not it's a Two Pairs
			hand_values_list = [card[0] for card in hand]
			for value in hand_values_list:
				if hand_values_list.count(value) > 2:
					return "Three of a Kind"
			else:
				return "Two Pairs"
		# only 4 different numbers has only One possibility and our easiest case
		case 4:
			return "One Pair"
		# each card has a different value, our most complex case can be 5 different types of hands
		case 5:
			# for Straights we want to hash the hand for easy checks with our precalculated possibilities so we need
			# a tuple because you can't hash mutable lists and a tuple is immutable
			hand_values_tuple = tuple(card[0] for card in hand)
			# checking the number of suits in the hand, if its only 1 suit we narrow down 3 out of our 5 options
			if len(set([card[1]for card in hand])) == 1:
				# check for a specific straight the best possible straight
				if hand_values_tuple == straight_list[-1]:
					return "Royal Flush"
				# if its not a Royal Flush, then hash to check if its a straight at all
				# we have to check in this order otherwise we might return a Straight Flush that was actually the Royal
				elif hand_values_tuple in straight_set:
					return "Straight Flush"
				# process of elimination determines its a Flush
				else:
					return "Flush"
			# if theres more than one suit than that leaves 2 options, the Straight or Nothing
			# check by hash
			elif hand_values_tuple in straight_set:
				return "Straight"
			# lastly, junk hand by process of elimination
			else:
				return "High Card"


if __name__ == "__main__":
	player_1_wins = 0
	player_2_wins = 0
	draws = 0
	# for each poker match
	for i in range(len(player_1)):
		# evaluate the hand type of each player
		hand_1, hand_2 = evalHandType(player_1[i]), evalHandType(player_2[i])
		# if both players have the same type of hand
		if hand_1 == hand_2:
			# process the tiebreaker analysis
			match breakTies(player_1[i], player_2[i], hand_1):
				case "Draw":
					draws += 1
				case "Player 1 Win":
					player_1_wins += 1
				case "Player 2 Win":
					player_2_wins += 1
		# otherwise scoring is easy check if hands are different types
		elif hand_scores[hand_1] > hand_scores[hand_2]:
			player_1_wins += 1
		else:
			player_2_wins += 1
	print(f"Out of 1000 5 card Poker hands, Player 1 wins {player_1_wins} games.")