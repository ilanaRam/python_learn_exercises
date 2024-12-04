from itertools import combinations, permutations, product

def cartesian_product(A,B): 
    my_cart_list = list(product(A,B))
    print(f"My cart list is: {my_cart_list}")
    # [(1, 3), (1, 4), (2, 3), (2, 4)]
    
    # Multiplexian works like - running in nested loop: 
    # for x in A:
    #   for y in B: 
    #       (x,y)

def main():
    A = [1,2]
    B = [3,4]

    cartesian_product(A,B)

if __name__ == '__main__':
    main()