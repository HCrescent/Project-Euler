"""Project Euler Problem 57 - Square root convergents"""


def iterateTwo(iterations):
	""" calculated the square root convergents for square root of two for any number of iterations

	:param iterations: Int - the number of iterations to calculate
	:return: Int - the number of results where the numerator has more digits than the denominator
	"""
	numers = [1, 3]
	denoms = [1, 2]
	for i in range(2, iterations+1):
		tmp_numerator = numers[-1] - denoms[-1]  # subtracting the one
		tmp_denominator = denoms[-1]  # the denominator of the previous result
		tmp_numerator += 2*tmp_denominator  # adding 2 for the continued fraction 2a
		# flipping the fraction here so 1/fraction == 1 * reciprocal
		tmp_numerator, tmp_denominator = tmp_denominator, tmp_numerator
		tmp_numerator += tmp_denominator  # adding back the one we took our earlier
		numers.append(tmp_numerator)
		denoms.append(tmp_denominator)
	# count the number of iterations where the numerator had more digits than its denominator
	larger_numerator_count = 0
	for i, each in enumerate(numers):
		if len(str(each)) > len(str(denoms[i])):
			larger_numerator_count += 1
	return larger_numerator_count


if __name__ == "__main__":
	ans = iterateTwo(1000)
	print("In 1000 expansions of sqrt2, the total fractions with more digits in the numerator than denominator is:", ans)
