"""Project Euler Problem 15 - Lattice paths"""
import time
start = time.time()


def recursivePath(bound, x=0, y=0):
	paths = 0
	if x < bound:
		paths += recursivePath(bound, x+1, y)
	if y < bound:
		paths += recursivePath(bound, x, y+1)
	if x == bound and y == bound:
		paths += 1
	return paths


if __name__ == "__main__":
	print(recursivePath(11))
	end = time.time()
	total_time = end - start
	print("\n" + str(total_time))
