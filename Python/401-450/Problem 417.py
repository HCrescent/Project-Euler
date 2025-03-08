"""Project Euler Problem 417 - Reciprocal Cycles II"""
import time
start = time.time()


def sieveEratosthenes(n):
    """ Generates a list of prime numbers up to inclusive n

    :param n: Int - the upper bound of primes we want
    :return: List - list of prime numbers up to n inclusive
    """
    # initialize the array for sieving, +1 to keep n included
    numbers = [True for _ in range(n+1)]
    # for 2 through floor of sqrt(n)
    for i in range(2, int(n**.5)+1):
        # if marked True it's our next prime
        if numbers[i]:
            # starting at prime squared, run through all multiples marking its composites false
            sub_run = i**2
            # make sure <= to allow n to be flagged appropriately
            while sub_run <= n:
                numbers[sub_run] = False
                sub_run += i
    # list comprehension to convert the boolean array into the meaningful information
    prime_array = [index for index, status in enumerate(numbers) if status]
    # skip 0 and 1 when returning the list
    return prime_array[2:]


# noinspection PyUnresolvedReferences
def primeFactorize(value):
    """Returns a list of prime factors of given whole number.

    :param value: int - number we are going to factorize
    :return: list - list of prime factors
    """
    prime_factors = []
    if value <= 1:
        return prime_factors
    try:
        # prime list exists with all prime numbers possibly needed to factor value
        assert prime_list
    except NameError:
        # prime list doesn't exist
        # always check 2 first
        number = 2
        # run until our value is reduced to 1
        while value > 1:
            # always start from the largest prime factor found last
            if len(prime_factors) > 0:
                number = prime_factors[-1]
            # while loop until you hit the first possible divisor, guaranteed to be prime
            # starts at 2 because 1 is not prime and always divisible
            # ends at sqrt of number (if largest factor is itself)
            while number <= value**.5:
                # if number divides evenly
                if value % number == 0:
                    # use floored division to prevent expanding int to float
                    value //= number
                    # append prime factor to list
                    prime_factors.append(number)
                    # breaks after first prime factor
                    break
                # this check is so we can include prime number 2 in our factor checks
                # if LSB of number is 1 we are odd and can skip all the rest of even numbers
                # else move from 2 -> 3
                if number & 1:
                    number += 2
                else:
                    number += 1
            # since we stopped early to save checking obviously wrong factors
            if number > value**.5:
                # at this point there are no more factors than our leftover value itself
                prime_factors.append(value)
                # lowering value to 1 to prepare to exit function
                value /= value
        return prime_factors
    # this section performs the same method as the trial division only
    # without checking any composite numbers by using the pre-calculated prime list
    prime_index = 0
    while prime_list[prime_index] <= value**.5:
        if value % prime_list[prime_index] == 0:
            prime_factors.append(prime_list[prime_index])
            value //= prime_list[prime_index]
            # don't increase the index, start from the last prime divisor
            continue
        prime_index += 1
    # append the final prime factor
    if value > 1:
        prime_factors.append(value)
    return prime_factors


def generateDivisors(powers, p_factors, div_list, factor=1, index=0):
    """ Recursive function that generates all divisors of a number given prime factors and their powers

    :param powers: List - an ordered list of power to match with the ordered list of prime factors
    :param p_factors: List - an ordered list of unique prime factors, to be paired with the powers list
    :param div_list: List - our list of discovered divisors
    :param factor: Int - factor to bring through function on our way to make a product for the final divisor
    :param index: Int - index marker for our variable length of expression terms
    :return: List - an updated list of all found divisors to be brought back up the stack and out of the first call
    """
    # reach the end of our variable length terms we have reached a product that is a divisor
    if index == len(powers):
        # append factor to our list of known divisor, return it up the stack
        div_list.append(factor)
        return div_list
    # for each in the current prime factors power range (ex if power is 2, range we want is 0, 1, 2)
    for each in range(powers[index]+1):
        # calculate the current term raised to (each)
        temp_factor = p_factors[index] ** each
        # multiply it by the factor brought in by the previous function call
        temp_factor *= factor
        # go deeper another call with the new temporary factor, to the next index position
        div_list = generateDivisors(powers, p_factors, div_list, temp_factor, index+1)
    # bring the list of known divisors up the stack
    return div_list


def product(values):
    """Takes an iterable and creates a product of each element in the iterable

    :param values: List - (or other compatible iterable) to get the product of all elements
    :return: Int - Calculated product
    """
    prod = 1
    for _ in values:
        prod *= _
    return prod


def phi(n):
    """ Euler's Totient function, positive integers up to n that are relatively prime to n

    :param n:
    :return: Int -
    """
    result = n
    p_dividing_n = list(set(primeFactorize(n)))
    for p in p_dividing_n:
        result *= (1 - 1/p)
    return int(result)


def allDivisors(value):
    """ Prepares the values required to calculate all divisors, passes them to calculate, then formats the result

    :param value: Int - the number we want to find all divisors of
    :return: List - the list of all calculated divisors of value
    """
    # get the list of prime factors
    prime_factor_list = primeFactorize(value)
    # make a condensed list of unique factors
    unique_prime_factors = list(set(prime_factor_list))
    unique_prime_factors.sort()  # the set function does not retain order so must be re-sorted
    # create a list of the powers of each unique prime factor
    factor_powers = [prime_factor_list.count(_) for _ in unique_prime_factors]
    # call the recursive function to calculate every permutation of prime factor powers product
    divisors_list = generateDivisors(factor_powers, unique_prime_factors, [])
    divisors_list.sort()
    return divisors_list


def rational_period(rational_denominator):
    """ returns the length of the period portion of the decimal representation of a rational [0,1)
    order of 10 mod c,  The order of a mod n is m if a^m ≡ 1 (mod n) if m is minimal

    :param rational_denominator: Int - rational denominator of the desired rational
    :return: Int - the number of digits in the period section of the decimal representation
    """
    factors = primeFactorize(rational_denominator)
    factors = [each for each in factors if each != 2 and each != 5]
    if factors:
        n = product(factors)
        max_possible_order = phi(n)
        plugins = allDivisors(max_possible_order)
        for test in plugins:
            if pow(10, test, n) == 1:
                return test
    return 0


if __name__ == "__main__":
    target = 1_000_001
    prime_list = sieveEratosthenes(round(target/2))
    period_sum = 0
    for N in range(3, target):
        period_sum += rational_period(N)
    print(period_sum)
    end = time.time()
    print(f"t:{end - start}")
