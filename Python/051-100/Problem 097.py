"""Project Euler Problem 97 - Large Non-Mersenne Prime"""


def fun(n):
	number = 1
	for _ in range(n):
		number *= 2
		number = number % 10_000_000_000
	return number

if __name__ == "__main__":
	result = fun(7830457)
	result *= 28433
	result += 1
	print(f"The last ten digits of the prime number 28433 * 2^7830457 + 1: {result % 10_000_000_000}")