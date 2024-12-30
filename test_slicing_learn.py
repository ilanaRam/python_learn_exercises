"""
Slicing training in python - slicing is the extraction of a part of a string, list or tuple 

object[start: stop: step]

list is mutable 
tuple is not mutable, it can be used for keys - as it locks the values!!
string is not mutable 
set is mutable but without repetitions (single occurance) 

"""
 
lst = [1,2,3,4,5,6,7,8,9,10]
tpl0 = tuple(lst)
tpl = (1,2,3,4,5,6,7,8,9,10)
s = 'Simple learn'
print(lst)
print(tpl)
print(tpl0)
print(s)

print(f"The last elem in list can be extracted by: {lst[len(lst)-1]} and also by: {lst[-1]}, one before is: {lst[-2]}")

print(f"get elems from beginning: {lst[0:3]}") # herewe start from 0 but last elem is at index 2 (3-1), last is not included 


print(f"get elems from beginning till the not existing index: {lst[0:100]}") # this will not allert but give all indexes from list 

# ---------------------------------------------------------------------------------
print(f"!!!!!!!! This is how we print 'Full array': {lst[:]}")
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"\'without the last elem': {lst[0:-1]}")
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\'from first but withou the last': {lst[:-1]}")
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"\'from first till the last': {lst[0:]}")
# [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

print(f"\'from the end of the list (reversed order) - take last 3 elems', then from sub list take all without last elem: {lst[-3:-1]}")
# [8, 9]

# ---------------------------------------------------------------------------------

print(f"\get last elem as elem: {lst[-1]}")
# 10

print(f"\get last elem as list: {lst[-1:]}")
# [10]

print(f"\n\nLets work with steps ...")
print(f"Print all array with default step (1): {lst[::]}")
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# REVERSE - when we use negative step - it means we go reverse order (the start is the last one)
print(f"Print all array with negative step (-1, it means array will be printed in reverse order): {lst[::-1]}")
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"\nGo from last elem [-1], till the first elem (means we go in reverse order) negative step - this will not change a thing,as we already started with last and we go in reversed order :")
print(f"{lst[-1::-1]}")
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print(f"\nGo from last elem [-3], till the first elem (means we go in reverse order), negative step = this will not change a thing,as we already started with last and we go in reversed order:")
print(f"{lst[-3::-1]}")
# [8, 7, 6, 5, 4, 3, 2, 1]

# the index 5 isnt included 
my_slice = slice(1, # start
                 5, # stop, 5 isnt included, it is up to 4
                 2) # step
print(f"auto sliced list is: {lst[my_slice]}")
# orig list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [2, 4]

# slicing with strings 
my_str = "Welcome to Simplilearn"
print(f"auto sliced string is: {my_str[my_slice]}")
# "ec"

# print the string in reverse order from last char (index -1), till the -12 (actually it is -11) with steps of 1 by 1
my_slice = slice(-1,
                 -12,
                 -1) # the index 5 isnt included 
print(f"auto sliced reversed string is: {my_str[my_slice]}")
# "nraelilpmiS"

sub_s = "to S"

print(f"Triying finding substring '{sub_s}' in the string: {my_str}")
res = my_str.find(sub_s) 
print(f"Index of first ocurance is: {res}")

