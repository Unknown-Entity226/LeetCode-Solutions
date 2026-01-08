'''Problem Description

Given an array of integers nums and an integer target, find the indices of two distinct elements such that their sum equals the target.
You may assume:
Exactly one valid solution exists
The same element cannot be used more than once
The result can be returned in any order

Approach:
Use a hash map to store previously seen numbers and their indices.
For each element:
Compute the difference between the target and the current number.
Check if this difference already exists in the hash map.
If it exists, return the stored index and the current index.
Otherwise, store the current number with its index in the hash map.

Time Complexity: O(n)
Space Complexity: O(n)'''

#Python Implementation
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_hash = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in num_hash:
                return [num_hash[diff], i]
            num_hash[num] = i
            


