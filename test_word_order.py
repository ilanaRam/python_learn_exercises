
from typing import List 
from math import pow
from collections import OrderedDict

MAX_CHARS_COUNT = pow(10,6)

class Words: 
    def __init__(self) -> None:
        self.words = OrderedDict()
        self.count_chars_per_word = 0        
        self.count_words = 0


    def get_input_amount_of_words(self:str)->None:
        while True: 
            line = input("Input number that represent amout of words: ").strip()            
            if not line:
                break
            elif not line.isnumeric():
                print(f"The input {line}, is not numeric")
                continue                  
            self.count_words = int(line)   
            break
        
        if self.count_words == 0:
            raise Exception("Amount of words was left - 0")


    def get_input_words_and_process(self)->None:  
        """
            the roles are: 
            all words should be lower case
            word will have only English letters
            sum of all characters in all words not more than 10^6
            per word - count num of characters and report output at the same order
            as they were received
        """      
        while self.count_words: 
            line = input("Enter word: ").strip().lower()            
            if not line:
                break
            if any(not element.isalpha() for element in line):
                print(f"The word {line}, has at least 1 characters that isnt an English letter") 
                continue                           
            
            if self.count_chars_per_word + len(line) > MAX_CHARS_COUNT:
                break
            self.count_chars_per_word += len(line)
            print(f"The chars in word: {line}, is: {len(line)}")

            # update counter per word
            self.words[line] = self.words.get(line,0) + 1  

            self.count_words -= 1
        
        print(f"The number of distinct words is: {len(self.words)}")
        [print(f"{count}") for count in self.words.values()]
    

if __name__ == '__main__':
    words_obj = Words()  
    words_obj.get_input_amount_of_words()
    words_obj.get_input_words_and_process()
   

    