
from collections import Counter


def find_triplets(arr):
    print("\nfind_triplets without ration\n ==============================")
    print(f"Input: {arr}\n")

    triplets_list = []
    my_dict = Counter(arr)

    for index in range(len(my_dict.keys())):
        # check that we do not jump over the array
        left_keys_dict_len = len(my_dict.keys()) - index
        if left_keys_dict_len < 3:
            break

        # take 3 elems, add them to t,p list
        tmp_keys_list = [*my_dict.keys()][index:index+3]
        triplets_list.append(tmp_keys_list)

        # check if even per 1 num in the triplet were duplicates add again the whole triplet
        for key in tmp_keys_list:
            if dict(my_dict)[key] > 1:
                triplets_list.append(tmp_keys_list)
    print(f" number of triplets is: {len(triplets_list)}, triplets: {triplets_list} \n\n")


# 1. find dict per number - to see its frequency
# 2. find for each number 2 numbers while between all them ration 3
# [ 1, 3, 9, 9, 27, 81 ]
# i = 1, j = 3,9 --> (1,3,9)  9 is 2 times so we have another triplet here (1,3,9)
# i = 3, j = 9, 27 --> (3,9,27)  9 is 2 times so we have another triplet here (3,9,27)
# i = 9, j = 27, 81 ---> (9,27,81) 9 is 2 times so we have another triplet here (9,27,81)

def find_geometric_progression(arr,ratio):
    print("\nfind_geometric_progression \n ==============================")
    print(f"Input: {arr}, ratio: {ratio}\n")

    arr = sorted(arr)
    my_dict = Counter(arr)
    triplets_list = []
    count = 0

    # per number find other 2 nums to build ration triplet
    for i in range(len(arr)):
        num = arr[i]
        # adding first elem t tmp list
        tmp_nums_list = []
        tmp_nums_list.append(num)

        for j in range(i+1, len(arr)):
            elem = arr[j]

            if not elem or \
                   elem == num or \
                   elem < num or \
                   tmp_nums_list and elem in tmp_nums_list:
                continue

            if elem // tmp_nums_list[-1] != ratio:
                continue

            if my_dict[elem] > 1:
                count += 1

            # when ration triplet is ready add it to list
            tmp_nums_list.append(elem)
            # per number find if it has duplications if so count how many

            if len(tmp_nums_list) == 3:
                # add 1 time
                triplets_list.append(tmp_nums_list)

                # add more times if were duplications
                for i in range(count):
                    triplets_list.append(tmp_nums_list)
                count = 0
                break

    print(triplets_list)
    print(f"The num of triplets is {len(triplets_list)}")




if __name__ == '__main__':
    #find_triplets([1,2,2,4], 2)
    find_geometric_progression([1,2,2,4], 2)

    #find_triplets([1, 3, 9, 9, 27, 81], 3)
    find_geometric_progression([1, 3, 9, 9, 27, 81], 3)

    # find_triplets([1, 5, 5, 25, 125], 5)
    find_geometric_progression([1, 5, 5, 25, 125], 5)


