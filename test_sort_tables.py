import math
import os
import random
import re
import sys





def my_athlets(): 
    
    nm = input("Please enter n for num of lines followed by m for num of items in line: ").rstrip().split()

    n_lines = int(nm[0])
    print(f"entered num of lines: {n_lines}")

    m_items_in_line = int(nm[1])
    print(f"entered num of elements in per line: {m_items_in_line}")

    arr = []

    for _ in range(n_lines):
        # receive a line from user
        elements_arr = input(f"Please enter line where will be {m_items_in_line} elements: ").rstrip().split()
        print(f"entered line: {elements_arr}")
                
        # convert all items in lin e to ints (as by def all that comes from cmd is strings)
        
        # aqppend list as element in upper list (will be list of sub lists)
        arr.append(list(map(int, elements_arr)))
        # the arr is: [[1, 11, 11], 
        #              [2, 22, 222]]

    print(f"the arr is: {arr}")

    k = int(input("Please - enter an index for sorting: ").rstrip())
    print(f"entered K: {k}")
    
    print(f"Sorting each element of ar by index: {k} ...")

    sorted_arr = sorted(arr, 
                        key=lambda item_in_arr: item_in_arr[k],
                        reverse=False)
    print(f"Sorted arr: {sorted_arr}")

if __name__ == '__main__':
    my_athlets()