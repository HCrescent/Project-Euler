"""Project Euler Problem 8 - Largest product in a series"""
import numpy as np

input_string = "73167176531330624919225119674426574742355349194934" \
               "96983520312774506326239578318016984801869478851843" \
               "85861560789112949495459501737958331952853208805511" \
               "12540698747158523863050715693290963295227443043557" \
               "66896648950445244523161731856403098711121722383113" \
               "62229893423380308135336276614282806444486645238749" \
               "30358907296290491560440772390713810515859307960866" \
               "70172427121883998797908792274921901699720888093776" \
               "65727333001053367881220235421809751254540594752243" \
               "52584907711670556013604839586446706324415722155397" \
               "53697817977846174064955149290862569321978468622482" \
               "83972241375657056057490261407972968652414535100474" \
               "82166370484403199890008895243450658541227588666881" \
               "16427171479924442928230863465674813919123162824586" \
               "17866458359124566529476545682848912883142607690042" \
               "24219022671055626321111109370544217506941658960408" \
               "07198403850962455444362981230987879927244284909188" \
               "84580156166097919133875499200524063689912560717606" \
               "05886116467109405077541002256983155200055935729725" \
               "71636269561882670428252483600823257530420752963450"
# format the large string into an array of integers
series = np.array(list(map(int, input_string)))


def largest_window_product(size, main_array):
    """ Finds the largest product in a sliding window of a large string of numbers, and its window

    :param size: Int - How large we want our sliding window to be
    :param main_array: np.array - a list of our integers to slide our window across
    :return: np array, int - the 13 adjacent digits and their product
    """
    inputs_array = []
    outputs_array = []
    start = 0
    end = size
    while end <= main_array.size:
        # save the processed array for indexing purposes and curiosity
        inputs_array.append(main_array[start:end])
        # if you don't specify the data type, numpy defaults to 32bit int which makes our program fail
        outputs_array.append(np.prod(main_array[start:end], dtype=np.int64))
        start += 1
        end += 1
    # get the index of the maximum product so we can also know where the corresponding array input is
    i = outputs_array.index(max(outputs_array))
    return inputs_array[i], outputs_array[i]


if __name__ == "__main__":
    # output the array itself for curiosity's sake
    print("The largest product of 13 adjacent digits is: ", largest_window_product(13, series))
