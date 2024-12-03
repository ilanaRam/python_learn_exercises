from functools import reduce
import math
from fractions import Fraction


# first arg - initial (is optional arg) if used must be most left argument
# second arg - here will be sent list item (if without initial at first time will be sent 2 first list items and each next time
# will be sent (tmp_sum, next list item))
  
def sum_func(tmp,          
             item_from_list):  
    print(f"Received tmp: {tmp}, item_from_list: {item_from_list}")
    new_sum = tmp + item_from_list

    print(f"Calculated new tmp sum and returned: {new_sum}\n")
    return new_sum

def multiply_func(a,b): 
    return a*b

def find_bigger_func(a,b):
    return a if a>b else b

def find_smaller_func(a,b):
    return a if a<b else b

def concat_two_strings(a,b):    
    return f"{a}{b}"

# !!!!!
def num_of_ccurances_func(cnt_to_update,   # !! initial - must be located as most left argument
                          item_from_list): # then item from a list
    # way 1 ternaric if:
    # return cnt_to_update + 1 if item_from_list == 3 else cnt_to_update
    
    # way 2:
    if item_from_list == 1:
        return cnt_to_update + 1
    else:
        return cnt_to_update

# way1:
    # 1. convert item to a list of single item,
    # 2. add new list that you build to it 
    # 3. return the new list that you build step by step

# way2: user new_list.insert(0,item_from_list)

def revers_func(new_list,
                item_from_list):    
    new_list = [item_from_list] + new_list
    return new_list
    
def flatten_func(empty_new_list, 
                 item_from_orig_list):    
    # Isimply unpacking the sub list and build new flatten list
    return empty_new_list + [*item_from_orig_list]

def sum_squares_func(squares_sum, item_from_list):    
    print(f"squer sum: {squares_sum}, item from list: {item_from_list} (squered item is: {item_from_list**2})")
    print(f"sum of squares: {squares_sum + item_from_list**2}\n")
    
    return squares_sum + item_from_list**2

def gcd_finder_func(tmp, 
                    item_from_list):
    new_gcd = math.gcd(tmp,item_from_list)
    return new_gcd

def fractonal_nums_product_func(tmp,
                                item_from_list):    
    return tmp * item_from_list

# ============================================================


if __name__ == '__main__': 

    my_list = [1,2,3,4,5]
    

    # sum list items
    my_sum = reduce(sum_func, 
                    my_list)
    print(f"The sum of the list is: {my_sum}")



    # sum squares(numbers) in a list
    my_sum_of_squares = reduce(sum_squares_func, 
                               my_list,
                               0)
    print(f"The sum of squares is: {my_sum_of_squares}")



    # make multiply list items
    my_mult = reduce(multiply_func, my_list)
    print(f"The multiply of the list is: {my_mult}")



    # Find biggest item in the list 
    my_big = reduce(find_bigger_func, my_list)
    print(f"The bigest element in the list is: {my_big}")



    # Find smallest item in the list
    my_small = reduce(find_smaller_func, my_list)
    print(f"The smallest element in the list is: {my_small}")



    # Concatenate all strings in the list
    list_of_strings = ["HELLOW", " ", "WORLD", " ", "I", " ", "am", " " ,"here"]
    concatinated_list = reduce(concat_two_strings, list_of_strings)
    print(f"Concatinated string is: {concatinated_list}")



    # !!!!
    # Find number of occurences of item in the list
    # !!!! reduce can get maximum 3 items - the third one is 'initial'
    items_lst = [1, 2, 3, 4, 1, 5, 1, 6 ,1] # here we have 1, 4 times    
    num_of_ccurances = reduce(num_of_ccurances_func, # the func that will work with the list and will do all the work
                              items_lst,             # a list to work with                                                 
                              0)                     # 'initial' = here we set it with 0 as initial value for cnt    
    print(f"The amount of occurances of item 1 in the list is: {num_of_ccurances}")



    # Reverse the list    
    items_lst = [1, 2, 3, 4]    
    new_list = reduce(revers_func, 
                      items_lst,
                      [])  # initial empty list - I will build this list          
    print(f"The reversed list is: {new_list}")



    # Flatten the list of lists to be: [1,2,3,4,5,6,7,8,9]  
    d3_lst = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]      
    new_list = reduce(flatten_func, 
                      d3_lst,
                      [])  # initial empty list - I will build this flatten list          
    print(f"The flatten list is: {new_list}")



    # Find GCD - greates common devider 
    my_list = [4,4,4,4,3]
    my_gcd = reduce(gcd_finder_func, 
                    my_list)
    print(f"The gcd is: {my_gcd}")


    # Find product of fractional nums (exp: 1/2*3/4*10/6 = 5/8)  
    my_list = [Fraction("1/2"), Fraction("3/4"), Fraction("10/6")]
    my_product = reduce(fractonal_nums_product_func, 
                        my_list)
    print(f"The gcd is: {my_product}")

