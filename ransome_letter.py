from collections import Counter

def my_check(magazine_sentence,
             my_sentence):
    print(f"Called my_check()")
    print(f"orig: {magazine_sentence}")
    print(f"my: {my_sentence}")

    # check is None is a correct way !!!
    if my_sentence is None or \
       magazine_sentence is None or \
       not magazine_sentence or \
       not my_sentence:
        print(f" bad string")
        return
    # build a dict from a list
    magazine_dict = dict.fromkeys(magazine_sentence.split())
    print(f"magazine sentence has the next words: {magazine_dict}")

    my_dict = dict.fromkeys(my_sentence.split())
    print(f"my sentence has the next words: {my_dict}")

    if len(magazine_dict) != len(my_dict):
        print(f"not good")
        return

    for my_key in my_dict.keys():
        if my_key not in magazine_dict.keys():
            print(f"not good")
            break
    else:
        # we got here because for loop never breaked = all keys were found
        print(f"good")

if __name__ == '__main__':
    magazine_sentence = "I am too pretty for Python"
    my_sentence0 = None
    my_sentence1 = ""
    my_sentence2 = "python is very pretty"
    my_sentence3 = "I am too pretty for python"
    my_sentence4 = "I am too pretty for pretty Python"
    my_sentence5 = "I too pretty for Python"
    my_sentence6 = "Python for pretty I am too" # reversed order

    # my way
    my_check(magazine_sentence, my_sentence0)
    my_check(magazine_sentence, my_sentence1)
    my_check(magazine_sentence, my_sentence2)
    my_check(magazine_sentence, my_sentence3)
    my_check(magazine_sentence, my_sentence4)
    my_check(magazine_sentence, my_sentence5)
    my_check(magazine_sentence, my_sentence6)
