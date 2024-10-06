from collections import Counter


def how_many_pairs_comprehension(socks_list):

    # create new iterable - soc = key, value = count
    my_dict = {soc: socks_list.count(soc)
               for soc in set(socks_list)}
    print(f"{my_dict}")

    pairs = 0
    lefts = 0

    for val in my_dict.values():
        pairs += int(val / 2)
        lefts += int(val % 2)

    print(f"pairs: {pairs}")
    print(f"lefts: {lefts}")


def how_many_pairs_counter(socks_list):

    # create new iterable - of type dict with nick keys and values (count)
    my_dict = Counter(socks_list)
    print(f"{my_dict}")

def how_many_pairs_long(socks_list):
    print(f'{socks_list}')

    # create only keys
    types_set = set(socks_list)
    print(f"Types of socks are: {types_set}")

    # convert set into dict
    types_dict = dict.fromkeys(types_set, 0) # 0 is value per key, this way I initiate a dict
    print(f"Dict of types of socks is: {types_dict}")

    pairs = 0
    lefts = 0
    # iterate keys and update values
    for soc_type in types_dict.keys():
        cnt = 0
        for soc in socks_list:
            if soc_type == soc:
                types_dict[soc_type] += 1

        # per soc I know amount
        pairs += int(cnt / 2)
        lefts += int(cnt % 2)
    print(f"dict: {types_dict}")
    print(f"pairs: {pairs}")
    print(f"lefts: {lefts}")

def how_many_pairs_short(socks_list):
    types_dict = {}
    for soc in socks_list:
        if soc in types_dict:
            types_dict[soc] += 1
        else:
            types_dict[soc] = 1

    print(f"Types of socks are: {types_dict}")

    pairs = 0
    lefts = 0

    for socs in types_dict.values():
        pairs += int(socs / 2) # or simply do: // which means integer division
    #     lefts += int(socs % 2)

    print(f"pairs: {pairs}")
    print(f"lefts: {lefts}")

def num_of_pairs(socks_list):
    socks_dict = {}
    num_of_sock_pairs = 0

    for sock in set(socks_list):

        socks_dict[sock] = socks_list.count(sock)
        num_of_sock_pairs += socks_list.count(sock) // 2

    print(f"the dict is: {socks_dict}")
    print(f"Number of Sock pairs is : {num_of_sock_pairs}")




if __name__ == '__main__':
    socks_list = [1, 2, 1, 2, 1, 3, 2, 3]
    print(f'{socks_list}')

    socks_list_1 = [1]
    print(f'{socks_list_1}')

    num_of_pairs(socks_list)

    # how_many_pairs_long(socks_list)
    how_many_pairs_short(socks_list)
    how_many_pairs_counter(socks_list)
    # how_many_pairs_comprehension(socks_list_1)
    #get_input()


