


def main():
    my_str = input().strip()

    # all the ways to get characters as a list from string

    # unpacking
    # my_str = [*my_str]

    # list comprehension
    # my_str = [character for character in my_str]

    # translation into list
    # my_str = list(my_str)

    # slicing
    my_list = []
    my_list[:] = my_str

    my_tuple = tuple(my_str) # this way we will have tuple of chars
    print(my_tuple)

    # convert chars from a string into integers by map, map returns iterable that we can convert into list/tuple/ ...
    my_tuple = tuple(map(int,my_str))  # this way we will have tuple of chars
    print(my_tuple)

    my_hash = hash(my_tuple)
    print(my_hash)


if __name__ == '__main__':
    main()