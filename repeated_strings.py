
def count_chars(my_str, n):
    print(f"received str: {my_str}, n: {n}")

    if not my_str or my_str is None:
        print(f"bad str: {my_str}")
        return
    if n < 0:
        print(f"bad val for n, {n}")
        return
    if len(my_str) > n:
        # original str too long, need to shorten string by m chars
        m = len(my_str) - n
        my_str = my_str[:-m] # new string is orig string without last m chars (from the end of the string take m
        print(f"string: {my_str}")
    else:
        # original str is too short, need to lengthen
        m = n//len(my_str) # write string m times
        mod = n%len(my_str) # addition
        my_str = (my_str * m) + my_str[:mod]
        print(f"string: {my_str}")
    counter = my_str.count('a')
    print(f"char a, found {counter} times")

if __name__ == '__main__':
    my_str = "aba"
    my_str1 = ""
    my_str2 = "abaabaababbbbbbbbbbba"
    n = 10 # find nums of char 'a' in n first chars of the string written repetitively
    count_chars(my_str,n)
    count_chars(my_str1,n)
    count_chars(my_str2,n)