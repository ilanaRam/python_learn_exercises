from itertools import combinations
from functools import reduce

def find_pair_with_given_sum_from_list(my_sorted_list, my_sum):
   
    # way1: use module combinations from itertools 
    
    # all_combs = combinations(my_sorted_list,2)
    # [print(comb) 
    #  for comb in all_combs
    #  if sum(comb) == my_sum]
    
    # way2: lets count a fact that the list is already sorted !!
    for item in my_sorted_list:
        for next_item in my_sorted_list[item:]:
            if item + next_item == my_sum:
                print(item,next_item)
                
# learn how to use eval build in func !!!
def try_eval_build_in_python_func(): 
    print(eval(input("enter sum expression please: ").rstrip()))
    # we get this: 
    
    # enter sum expression please: 3+5*4
    # the result is: 23
def zip_func_try():
    my_l = [1,2,3,4,5,6]
    my_s = 'Hacker'
    print(f"The zipped is: {list(zip(my_l,my_s))}") 
    #The zipped is: [(1, 'H'), (2, 'a'), (3, 'c'), (4, 'k'), (5, 'e'), (6, 'r')]

    # zip goes by the shortest list, so all others from long are dropped !!
    print(f"The zipped: {list(zip([1,2,3,4,5,6],[0,9,8,7,6,5,4,3,2,1]))}")
    #[(1, 0), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5)]

    A = [1,2,3]
    B = [6,5,4]
    C = [7,8,9]
   
    print(f"By adding this way: [A] + [B] + [C], will be created list of list: matrix: {[A] + [B] + [C]}")
    # will be createds a list of lists
    # [[1, 2, 3], [6, 5, 4], [7, 8, 9]]

    a1 = A + B + C # all lists will be build 1 big list    
    a3 = [A] + [B] + [C]
    a2 = [*A,*B,*C]  # all lists will be unpacked and will be created one big list
    print(f"\n\nBy adding this way: A + B + C, will be created list with all elems uppacked: {a1}")    
    print(f"By adding this way: a3 = [C] + [B] + [C], zip(*a3) is: {list(zip(*a3))} = {list(zip(A,B,C))}")    
    print(f"By adding this way: [*A,*B,*C], will be created list with all elems uppacked: {a2}")    


def sum_func(init_sum, elem):
    local_average = sum(elem) / len(elem) 
    print(f"local_average: {local_average}")    
    local_sum = init_sum + sum(elem)
    print(f"local_sum: {local_sum}")    
    return local_sum  

def find_average_score():
    s1 = [89,    90,    78,    93,    80]
    s2 = [90,    91,    85,    88,    86]
    s3 = [91,    92,    83,    89,    90.5]

    zipped_s = list(zip(s1, s2, s3))
    print(f"zipped s: {list(zipped_s)}")
    
    averages = [sum(elem) // len(elem) for elem in zipped_s]
    print(f"average = {averages}")
   



if __name__ =='__main__':
    # list is already sorted !!!!
    find_pair_with_given_sum_from_list(my_sorted_list = [1,2,3,4,5,6], my_sum=7)
    try_eval_build_in_python_func()

    zip_func_try()
    find_average_score()