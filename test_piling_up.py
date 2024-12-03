# building are kind of matrixes 
import math
import os
import random
import re
import sys
from collections import OrderedDict


if __name__ == '__main__':
    my_s = None
    my_d = []
    

    while True: 
        my_s = input("please enter string S: ")
        if not my_s: 
            break   
        my_d = {item: my_s.count(item) for item in my_s}
        print(f"The dict is: {my_d}")

        my_d2 = OrderedDict(my_s)
        print(f"The dict is: {my_d2}")

        if len(my_d) < 3: 
            print(f"The input must be at least 3 'different' characters")
        else:
            break
    
    if not my_d: 
        exit()
    print(f"The max item in my dict is: {max(my_d.keys())}")

    



