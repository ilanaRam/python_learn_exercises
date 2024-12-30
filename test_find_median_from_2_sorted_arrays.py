from typing import List
import math

class Solution(object):
    """
    # median is a member that stands in the middle of the list
    # if number of elements is even, then it is avg of 2 elems in the middle
    # if number of elements is odd, then it is the elem in the middle
    """
    def findMedianSortedArrays(self, nums1: List, nums2: List): 
        # The solution is very easy - add both lists - create 1 list, sort it, find meadian !!

        # combine lists into 1 list (list will come after a list)
        new_list = nums1 + nums2
        print(f"the new list = {new_list}")

        # sort again the new list
        new_list = sorted(new_list)
        print(f"the new list = {new_list}")
        
        # find median item
        if len(new_list) % 2 == 0: 
            index1 = len(new_list) // 2 - 1
            index2 = len(new_list) // 2 
            mid_item = (new_list[index1] + new_list[index2]) / 2            
        else: 
            index = len(new_list) // 2
            mid_item = new_list[index] 

        print(f"the mid item = {mid_item}")

    


if __name__ == '__main__':
    obj = Solution() 

    nums1 = [1,3]
    nums2 = [2]  
    print(f"list1 = {nums1}")
    print(f"list2 = {nums2}") 
    un_list = obj.findMedianSortedArrays(nums1, nums2)

    nums1 = [2]
    nums2 = [1,3] 
    print(f"list1 = {nums1}")
    print(f"list2 = {nums2}")      
    un_list = obj.findMedianSortedArrays(nums1, nums2)

    nums1 = [1,2]
    nums2 = [3,4]   
    print(f"list1 = {nums1}")
    print(f"list2 = {nums2}") 
    un_list = obj.findMedianSortedArrays(nums1, nums2)

    nums1 = [1,3]
    nums2 = [2,4]    
    print(f"list1 = {nums1}")
    print(f"list2 = {nums2}")
    un_list = obj.findMedianSortedArrays(nums1, nums2)