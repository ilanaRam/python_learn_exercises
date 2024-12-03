import re

#==================================================
# re.split(regex_string, string to split into list)
# finds element by defined regex and then splits string by regex to elements in list
#==================================================
# exp: pattern = r'[,]\s*'  , with white spaces
# str = 100,000,000
# mylist = re.split(pattern,str)
# result:
# mylist = [100,000,000]


def re_split_func():
    number_str = '100,000,000,000'
    pattern_for_split = r'[,]\s*' # [here we define all the options we might meat]
    # \s means if around match will be white space (or several white spaces) - it is ok too

    # if the input is: 100,000,000,000
    # the output should be:
    # 100
    # 000
    # 000
    # 000
    my_number_list = re.split(pattern_for_split, number_str)
    print(my_number_list)



#==================================================
# re.search	Returns a Match object if there is a match anywhere in the string
#==================================================

#==================================================
# find if match can be found at the beginning of the string
#re.match(r'regex', string )
#==================================================

#==================================================
# find if entire string is matches the regex rule else returns non
#re.fullmatch(r'regex', string )
#==================================================

def is_floating_number():

    """
    Number can start with + / - / .

    V +4.50
    V -1.0
    V .5
    V -.7
    V +.4
    V 12.0
    X -+4.5
    X 12.
    X 12..
    X 12..0
    Number must not give any exceptions when converted using  float(N)
    """
    inputs = [
        "+45",  # True
        "+4.5",  # True
        "-4.50",  # True
        "-+4r.0",
        "-+4.0",
        "-+-4.0",
        ".",# False
        ".5",# False
        "+.5",# False
        ".+5",# False
        "5.",# False
        "+.",# False
    ]
    # Regex pattern for floating-point numbers
    # ? after something mean that "something" is optional can appear or can not appear
    # hear means that or + or - can or cannot start the number
    # \d means any digit 0-9
    # | means or
    # ? means optional (can appear or not)
    # this option: \d+(\.\d*)? digit  (+:1 or n times) then optional: . followed by digit (*:0 or more times)
    # = decimal number exp: 4.55 or 4
    # or
    # this option: \.\d+: can be .<number> (1 or more times) .4, .45, .100
    # then (\d+(\.\d*)?   |    \.\d+)
    pattern  = r'^[+-]?(\d+(\.\d*)?|\.\d+)$'
    pattern1 = r'^[+-]?(\d+\.\d*?|\.\d+)$'

    results = []

    for elem in inputs:
        if re.fullmatch(pattern1, elem) is not None:
            results.append((elem, True))
        else:
            results.append((elem, False))

    print(results)
    return results


def way_1_for_in_for(my_str):
    print(f"way1")
    # by dict
    # my_set = set(my_str)

    # my_list = [char for char in my_str]
    my_list = list(my_str)
    print(f"my_list: {my_list}")
    count = 1
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if my_list[i] == my_list[j]:
                count += 1
                print(f" the first repetitive char is {my_list[i]}")
                break
        else: #under 'else' we define operations to be executed when for loop was not breaked !!
            continue
        break

def way_2_by_count_elem_in_rest_string(my_str):
    print(f"way2")
    my_list = list(my_str)
    print(f"my_list: {my_list}")

    for i in range(0,len(my_list)):
        if my_list[i+1:].count(my_list[i]) > 1:
            print(f"{my_list[i]} appears more than 1 time")
            break


def find_first_repettetive_number():
    # we ask to return a group (specific part from the matched result)
    # we build pattern - here we define groups
    # we apply it on the input -> this brings us a resulted string if there is a match
    # From the result we can ask to give us group

    my_str = "12345678910111213141516171820212223"
    print(f"my_str: {my_str}")
    # return first repetitive character - here it is 111 therefore it is 1

    way_1_for_in_for(my_str)
    way_2_by_count_elem_in_rest_string(my_str)



def main():

    # Read from multiple command line input, each input in new line
    # lines = []
    #
    # while True:
    #     line = input().strip()
    #
    #     # not empty line (can be if on empty line we will press Enter)
    #     if line:
    #         lines.append(line)
    #     else:
    #         break
    #
    # # this is a convertion list to string, where each elem is separated by Enter - just for printing
    # text = '\n'.join(lines)
    # print(text)


    # is_floating_number()
    # re_split_func()
    find_first_repettetive_number()


if __name__ == '__main__':
    main()

