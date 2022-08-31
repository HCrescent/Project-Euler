"""Project Euler Problem 17 - Number letter counts"""
singles = {'0': "", '1': "one", '2': "two", '3': "three", '4': "four",
           '5': "five", '6': "six", '7': "seven", '8': "eight", '9': "nine"}
tens = {'0': "", '1': "", '2': "twenty", '3': "thirty", '4': "forty",
        '5': "fifty", '6': "sixty", '7': "seventy", '8': "eighty", '9': "ninety"}
teens = {'0': "ten", '1': "eleven", '2': "twelve", '3': "thirteen", '4': "fourteen",
         '5': "fifteen", '6': "sixteen", '7': "seventeen", '8': "eighteen", '9': "nineteen"}
hundred = "hundred"
conjunction = "and"


def numberString(number):
    """ Creates a string of written out number for up to 3 digits

    :param number: Int - The integer we want to turn into written words
    :return: Str - The finished composed string (no whitespace, for simplicity of the problem)
    """
    instance_string = ""
    num_str = str(number)
    # make sure our analytical string is 3 digits
    if len(num_str) < 3:
        num_str = num_str.zfill(3)
    num_list = list(num_str)
    instance_string += singles[num_list[0]]
    # if our instance string is not empty we need to add the hundred word
    if len(instance_string) > 0:
        instance_string += hundred
        # if we are above 100, we need to test digits 2 and 3 for the need of AND conjunction
        if num_list[1] != '0' or num_list[2] != '0':
            instance_string += conjunction
    # if tens digit is a one we need special names
    if num_list[1] == '1':
        instance_string += teens[num_list[2]]
    # else add the standard word definitions
    else:
        instance_string += tens[num_list[1]]
        instance_string += singles[num_list[2]]
    return instance_string


if __name__ == "__main__":
    # start with the letter count for special case 1000
    accumulator = 11
    for _ in range(1, 1000):
        accumulator += len(numberString(_))
    print("All numbers 1 to 1000 (one thousand) inclusive written out in words,"
          " takes", accumulator, "alphabetical characters.")
