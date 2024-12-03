from itertools import combinations, permutations

##################################################################################
#  in this excersize we will work only with combinations (without repetitions)   #
#  result also need to be sorted and ordered (it is easy !!)                     #
##################################################################################

def get_input():

    while True: 
        my_in = input("Please enter input in this format: string number: ")
        print(f"The input is: {my_in}")

        try: 
            # input     
            if not my_in: 
                print(f"The input is empty, the app is finished ##")
                break  
            my_str , num = my_in.split()   
            
        except Exception as e:
            print(f"error occured during input: {e}")
        else:            
            try:
                # checking correctness of the input
                my_new_str = my_str.upper()
                num = int(num)
            except Exception as e:
                print(f"error occured during checking correctness of the input: {e}")
            else: 
                break

    return my_new_str, num

def print_permutations(my_str, k): 
    
    if not my_str or not k:
        exit   
    

    # # permutations - you will get all posible permutations - even if there will be repetitions 
    # my_list = list(permutations(str,k))
    # print(f"my list of all permutations (includes repetitions) is: {my_list}")
    # # this what we will get in case k = 1:   [('a',), ('b',), ('c',), ('d',), ('e',)]
    
    # my_list = list(combinations(str,k)) 
    # print(f"my list of all combinations (means without repetitions) is: {my_list}", end='\n')
    # # this what we will get in case k = 1:   [('a',), ('b',), ('c',), ('d',), ('e',)]

    # first for is runs on length of combinations
        # combinations with 1 elem in each ('a',), ...
        # combinations with 2 elems in each ('a', 'c'), ...
        # combinations with 3 elem in each ('a', 'c', 'h'), ...
        # combinations with 4 elem in each ('a', 'c', 'd','h')

    """ 
        in case k = 1
        a
        c
        h
        k

        in case k = 2
        ac
        ah
        ak
        ch
        ck
        hk
   
        in case k = 3
        ach
        ack
        ahk
        chk
    """
    for i in range(1,k + 1):
        for combo in combinations(sorted(my_str), i):
            print(f"{''.join(combo)}")
            # print(f"{combo}") this way we will get ('A','B')
            # print(list(combo)) here we will get: ['A', 'K'] .....
    



def main():
    my_str, my_number = get_input() 
    print_permutations(my_str, my_number) 
    



if __name__ == '__main__':
    main()

    