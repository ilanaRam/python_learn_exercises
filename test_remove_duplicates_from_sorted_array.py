# from leetcode
# Problem: Remove Duplicates from Sorted Array
# Description:
# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in nums

from typing import List
import pytest

expected_nums: List[int] = [1,2,3,4]
expected_nums_len = len(expected_nums)

class Solution(object):
    def test_removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print("The original nums is:")
        print(nums)
        
        nums = set(nums)
        print(f"The nums without duplicates is: {nums}")
        print(f"The length of the not duplicates nums is: {len(nums)}")         
        return len(nums)


if __name__ == '__main__':
    my_obj = Solution()
    my_len = my_obj.test_removeDuplicates([1,1,2,3,3,4])
    assert my_len == expected_nums_len, "Incorrected expected len of the not duplicated list"
    print(my_len)

        