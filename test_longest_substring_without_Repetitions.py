


"""
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
"""

class SubString: 
    def __init__(self) -> None:
        pass
    
    def find_longest_substring_without_repetitions(self, my_str: str) -> int: 
        print(f"The string to deal with: {my_str}")

        max_len: int = 0
        last_char: str = None
        curr_len: int = 0

        existing_chars = []
        max_sequence = []

        for curr_char in my_str:                                     
            print(f"\nLast char was: {last_char}, the current char: {curr_char}")
            print(f"The max length is: {max_len}")
            
            if curr_char not in existing_chars:
                existing_chars.append(curr_char)  
                print(f"The list of chars so far: {existing_chars}")              
                
                curr_len = len(existing_chars)# += 1
                print(f"current lenght: {curr_len}")
            else:
                existing_chars.clear()   # existing_chars = []
                existing_chars.append(curr_char)
            
            if max_len < curr_len: 
                    max_len = curr_len                    
                    curr_len = 0
                    max_sequence = existing_chars.copy() # !!!! else the next .clear() will clear both lists
                    
            # store last char 
            last_char = curr_char

        print(f"The max found length is: {max_len}, the max sequence is: {max_sequence} \n***********\n")

if __name__ == '__main__': 
    my_obj = SubString()
    my_obj.find_longest_substring_without_repetitions("abcbb")
    my_obj.find_longest_substring_without_repetitions("bbbbb")
    my_obj.find_longest_substring_without_repetitions("pwwkew")
    my_obj.find_longest_substring_without_repetitions("")
    my_obj.find_longest_substring_without_repetitions("re")
