"""Project Euler Problem 19 - Counting Sundays"""
# what do i need
# i need to be able to tell what the day of the week it is at any given date

standard_months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
leap_months = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
weekdays = {0: "Sunday", 1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
months_dict_list = [standard_months, leap_months]


def countFirstSundays():
	""" Counts the number of sundays that fell on the first of the month from jan 1901 to the end of 2000

	:return: Int - The total number of sundays
	"""
	year = 1900
	sundays = 0
	day = 1
	# prime our algorithm to jan 1st 1901
	while year < 1901:
		for i in range(13)[1::]:
			day += standard_months[i]
		year += 1
	# main counting loop
	while year < 2001:
		# identifying leap year logic
		if year % 100 == 0:
			if year % 400 == 0:
				leap = 1
			else:
				leap = 0
		elif year % 4 == 0:
			leap = 1
		else:
			leap = 0
		# checking the first of each month for sunday
		for month in range(13)[1::]:
			# check the first before we add a month worth of days
			if day % 7 == 0:
				sundays += 1
				# reset our accumulating day count to keep modulus division simple
				day = 0
			# add the call from the correct dict based on leap year or not
			day += months_dict_list[leap][month]
		year += 1
	return sundays


if __name__ == "__main__":
	print("The number of sundays on the first of the month, from Jan, 1st 1901 to Dec, 31st 2000:", countFirstSundays())
