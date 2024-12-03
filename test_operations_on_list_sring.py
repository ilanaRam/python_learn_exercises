import re

def split_and_join_strings():
    my_str = input("Enter a string: ")
    tmp_list = my_str.split(" ")
    print(f"splited str into list is: {tmp_list}")

    new_str = "-".join(tmp_list)
    print(f"joined str into list is: {new_str}")


def find_one_elem_before_max_in_list():
    my_list =  [2,3,6,6,5]


    # sorted(my_list) does not changes the list in place
    # my_list.sort() changes the list itself in place

    # print(my_list)
    # print(sorted(my_list))
    # print(my_list)


    my_list.sort()
    print(my_list)

    my_max = max(my_list)
    print(f"my max is: {my_max}")

    # build dict where per number you will have its dif from max number
    my_dict = {num: my_max - num
                  for num in my_list}
    print(my_dict)

    # run on diffs only - sort them, the smallest (but not 0) means that the number most close to max
    my_vals = my_dict.values()
    sorted_vals = list(my_vals)
    sorted_vals.sort()
    print(sorted_vals)

    for dif in sorted_vals:
        if dif > 0:
            print(dif)
            break



def mute_string():
    my_str = 'babayaga'
    print(f"original str is: {my_str}")

    # my_str[:-2]  => take all str from beginning without 2 last one chars
    # my_str[-2:]  => take only 2 last one chars

    new_str = my_str[:-2] + '-k-' + my_str[-2:]
    print(f"joined str is: {new_str}")


def find_student_with_second_lowest_grades():
    print("Please enter student name and grade: ")

    my_input = []
    res_list = []
    res_dict = {}

    while True:
        line = input().strip()
        if line:# not empty line (can be if on empty line we will press Enter)
            my_input.append(line)
        else:
            break

    # this is a convertion list to string, where each elem is separated by Enter - just for printing
    #text = '\n'.join(lines)

    print(f"the whole input is: {my_input}")
    if len(my_input) % 2 != 0:
        print("the input missing some details")
    else:
        print("the input is OK")
        for i in range(0,len(my_input),2):
            # check if first is string and second contains only numeric
            try:
                if not isinstance(my_input[i + 1], int):
                    raise ValueError

                res_dict[my_input[i]] = int(my_input[i + 1])
                print(f"saved new elem in dic: {my_input[i]} : {my_input[i + 1]}")
            except ValueError as err:
                print(err)
                continue

        print(f" res_dict is: {res_dict}")



def main():
    # split_and_join_strings(my_str)
    # mute_string()
    # find_one_elem_before_max_in_list()
    find_student_with_second_lowest_grades()

if __name__ == '__main__':
    main()
