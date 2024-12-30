



# we have:
# arra y with n integers
# 2 disjoint sets: A, B each has m integers. We like all ints in A and dont like all in set B!!
# initial happiness = 0
# you iterate through array ands per item in array you check if it is in A that happy +=1, if item in B then happy -=1, else ignot item. 



def check_item_in_any_array():
    happy_cnt = 0
    array = [10, 1, 2, 7, 4, 15, 20, 3]
    A = (1,70,4,80)
    B = (7,15,2,3)

    for item in array:         
        if item in A: 
            happy_cnt += 1
        elif item in B: 
            happy_cnt -=1
        else: 
            continue
    print(f"the happy cnt == {happy_cnt}")



if __name__ == '__main__': 
    check_item_in_any_array()
