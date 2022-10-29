"""Create new file for a Project Euler problem in Project Repo"""
import urllib.request
from urllib.error import HTTPError
from os import makedirs
import os.path
from os.path import isdir


def create_files(number):
    # force correct input format
    while True:
        try:
            number = int(number)
            break
        except ValueError:
            number = input("Please enter only an integer: ")
    # check for website response
    try:
        assert urllib.request.urlopen(f"https://projecteuler.net/problem={number}").getcode() == 200
    except HTTPError:
        print("Project Euler website did not return data at your input")
        return
    # grab page source
    lines_list = [line for line in urllib.request.urlopen(f"https://projecteuler.net/problem={number}")]
    # make sure the source has required data
    try:
        assert len(lines_list) > 1
    except AssertionError:
        print("got a code 200 but page source is empty")
        return
    # string formatting for header
    target_string = str(lines_list[8])
    header = target_string.split('#')[1].split(" - ")[0].split()
    header.insert(1, '-')
    header = ' '.join(header)
    title = "Problem " + f"{number}".zfill(3)
    # create starting path
    path = "../"
    # main section for finding the right placement and creating the script
    group_not_found = True
    while group_not_found:
        for folder in os.listdir(path)[:-1]:
            floor, ceiling = list(map(int, folder.split('-')))
            if number in range(floor, ceiling+1):
                script_path = path + folder + "/Problem " + f"{number}".zfill(3) + ".py"
                group_not_found = False
                break
        # if the group hasn't been found
        if group_not_found:
            # noinspection PyUnboundLocalVariable
            floor += 50
            # noinspection PyUnboundLocalVariable
            ceiling += 50
            new_path = f"../{floor}-{ceiling}"
            print("Path folders don't yet exist.")
            makedirs(new_path)
            print("Directories created.")
    # noinspection PyUnboundLocalVariable
    if not os.path.exists(script_path):
        with open(script_path, 'w') as new_file:
            new_file.write(f"\"\"\"Project Euler Problem {header}\"\"\"\n"
                           "\n"
                           "\n"
                           "def fun():\n"
                           "\tpass\n"   
                           "\n"
                           "\n"
                           "if __name__ == \"__main__\":\n"
                           "\tprint(fun())\n")
        print(f"Script {title}" + ".py created.")
        # check for additional input data
        target_line = [str(line) for line in lines_list if b'project/resources/' in line]
        if len(target_line) > 0:
            target_line = target_line[0]
        print(target_line)


        # noinspection PyUnboundLocalVariable
        input_path = path + folder + f"/text inputs/{title}" + ".txt"
        print(input_path)

    else:
        print(f"Script {title}" + ".py already exists.")
    #     if not os.path.exists(input_path):
    #         with open(input_path, 'w') as new_input:
    #             new_input.write("insert input here")
    #         print(f"Input input{day}.txt created.")
    #     return
    # print("files already exist")
    # return


if __name__ == "__main__":
    create_files(input("number: "))
