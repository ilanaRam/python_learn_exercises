from functools import reduce
import math
from fractions import Fraction
import pytest  # this one I need for using a fixture of setup_and_teardown()


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
    return a+b

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

def revers_func(item1, # we deliver the initialy the [] empty list
                item2):    
    new_list = [item2] + item1
    return new_list
    
def flatten_func(empty_new_list, 
                 item_from_orig_list):    
    # Isimply unpacking the sub list and build new flatten list
    return empty_new_list + [*item_from_orig_list]

def sum_squares_func(squares_sum, item_from_list):    
    print(f"squer sum: {squares_sum}, item from list: {item_from_list} (squered item is: {item_from_list**2})")
    print(f"sum of squares: {squares_sum + item_from_list**2}\n")
    
    return squares_sum + item_from_list**2

def gcd_finder_func(item1_from_list, 
                    item2_from_list):
    
    new_gcd = math.gcd(item1_from_list,
                       item2_from_list)
    return new_gcd

def fractonal_nums_product_func(tmp,
                                item_from_list):    
    return tmp * item_from_list

# ============================================================
my_list = [1,2,3,4,5]
@pytest.fixture(scope="module") # autouse=True
def setup_and_teardown():    
    print(f"Test - Started")    
    print(f"The list is ready to use: {my_list}")
    yield
    print(f"Test is - Done")


@pytest.mark.usefixtures("setup_and_teardown")
def test_sum_test_reduce():
    # sum list items
    my_sum = reduce(sum_func, 
                    my_list)
    print(f"The sum of the list is: {my_sum}")
    assert my_sum == 15


@pytest.mark.usefixtures("setup_and_teardown")
def test_sum_squers_reduce():    
    # sum squares(numbers) in a list
    my_sum_of_squares = reduce(sum_squares_func, 
                               my_list,
                               0)
    print(f"The sum of squares is: {my_sum_of_squares}")
    assert my_sum_of_squares == 55

@pytest.mark.usefixtures("setup_and_teardown")
def test_multipy_reduce():
    # make multiply list items
    my_mult = reduce(multiply_func, my_list)
    print(f"The multiply of the list is: {my_mult}")
    assert my_mult == 120

@pytest.mark.usefixtures("setup_and_teardown")
def test_find_bigest_reduce():
    # Find biggest item in the list 
    my_big = reduce(find_bigger_func, my_list)
    print(f"The bigest element in the list is: {my_big}")
    assert my_big == 5

@pytest.mark.usefixtures("setup_and_teardown")
def test_find_smallest_reduce():
    # Find smallest item in the list
    my_small = reduce(find_smaller_func, my_list)
    print(f"The smallest element in the list is: {my_small}")
    assert my_small == 1


@pytest.mark.usefixtures("setup_and_teardown")
def test_reverse_list():
    # Reverse the list    
    new_list = reduce(revers_func, 
                      my_list,
                      [])  # initial empty list - the new list will be started with first item - which is a list of single item - empty list          
    print(f"The reversed list is: {new_list}")
    assert new_list == [5, 4, 3, 2, 1]

    
def test_concat_all_strings_in_list_reduce():
    # Concatenate all strings in the list
    list_of_strings = ["HELLOW", " MY", " WORLD", " ", "I", " ", "am", " " ,"here"]

    concatinated_list = reduce(concat_two_strings, 
                               list_of_strings)
    print(f"Concatinated string is: {concatinated_list}")
    assert concatinated_list == "HELLOW MY WORLD I am here"


def test_find_num_of_occurences_item_in_list():
    # !!!!
    # Find number of occurences of item in the list
    # !!!! reduce can get maximum 3 items - the third one is 'initial'
    items_lst = [1, 2, 3, 4, 1, 5, 1, 6 ,1] # here we have 1, 4 times    
    
    num_of_ccurances = reduce(num_of_ccurances_func, # the func that will work with the list and will do all the work
                              items_lst,             # a list to work with                                                 
                              0)                     # 'initial' = here we set it with 0 as initial value for cnt    
    print(f"The amount of occurances of item 1 in the list is: {num_of_ccurances}")
    assert num_of_ccurances == 4


def test_flatten_the_list():
    # Flatten the list of lists to be: [1,2,3,4,5,6,7,8,9]  
    d3_lst = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]    
      
    new_list = reduce(flatten_func, 
                      d3_lst,
                      [])  # initial empty list - I will build this flatten list          
    print(f"The flatten list is: {new_list}")
    assert new_list == [1,2,3,4,5,6,7,8,9]


def test_find_gcd():
    # Find GCD - greates common devider 
    my_list = [4,4,4,4,5]
    my_gcd = reduce(gcd_finder_func, 
                    my_list)
    print(f"The gcd is: {my_gcd}")
    assert my_gcd == 1


def test_find_product_of_fractional_nums():
    # Find product of fractional nums (exp: 1/2*3/4*10/6 = 5/8)  
    my_list = [Fraction("1/2"), Fraction("3/4"), Fraction("10/6")]
   
    my_product = reduce(fractonal_nums_product_func, 
                        my_list)
    print(f"The gcd is: {my_product}")
    assert my_product ==  Fraction("5/8")  


# 11 tests: 
# test_flatten_the_list()
# test_sum_test_reduce()
# test_sum_squers_reduce()
# test_multipy_reduce()
# test_find_bigest_reduce()
# test_find_smallest_reduce()
test_concat_all_strings_in_list_reduce()
# test_find_num_of_occurences_item_in_list()
# test_reverse_list()
# test_find_gcd()
# test_find_product_of_fractional_nums()

# run these 11 test from Terminal by cmd: 
# pytest test_functools_module_reduce.py
   

    



    

