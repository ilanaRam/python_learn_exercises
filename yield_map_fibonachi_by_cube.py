


def fibo_gen(n): 
    a,b = 0,1

    while n:         
        yield a  
        tmp = b    # keep a side 'original' val of b
        b = a + b  # create a 'new' b from a sum of two previus
        a = tmp    # restore 'original' b val
        
        n -= 1

def create_fibonachi_seria(fibo_len):
    fibo_list = []
    
    # create generator (factory) for 5 fibo elems - it kind of 5 place holders 
    gen = fibo_gen(fibo_len)    

    # here we use the generator to generate each time new fibo elem
    for i in gen:       
       print(f"fibo elem received from gen:{i}")
       fibo_list.append(i)

    return fibo_list


if __name__ == '__main__': 

    leng = 5

    fibo_generated_list = create_fibonachi_seria(leng)
    print(f"The cubed fibo generated list is: {fibo_generated_list}")

    # way 1
    fibo_generated_list1 = list(map(lambda fibo_elem: fibo_elem**3, fibo_generated_list))
    print(f"The way 1 to cube fibo generated list is: {fibo_generated_list1}")

    # way 2
    cube = lambda x: x**3

    fibo_generated_list2 = list(map(cube, fibo_generated_list))
    print(f"The way 2 to cube fibo generated list is: {fibo_generated_list2}")
