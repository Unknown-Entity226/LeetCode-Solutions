"""
Problem Description:
Given an integer array, find the smallest index i such that the sum of
the digits of nums[i] is equal to i. Return -1 if no such index exists.

Approach:
- Define a helper function to calculate the digit sum of a number.
- Traverse the array from left to right.
- For each index, calculate the digit sum of nums[i].
- If the digit sum equals the current index, immediately return the index.
- Since indices are checked in increasing order, the first valid index is
  guaranteed to be the smallest one.
- Return -1 if no valid index is found.

Time Complexity:
O(n * d)

Reason:
- We examine each of the n elements.
- Calculating the digit sum takes O(d), where d is the number of digits.
- Therefore the total complexity is O(n * d).

Space Complexity:
O(1)

Reason:
- Only a constant amount of extra space is used by the digit_sum function.
"""

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        def digit_sum(n):
            s = 0
            while n:
                s+= n%10
                n//=10

            return s

        for i in range(len(nums)):
            if digit_sum(nums[i]) == i:
                return i

        return -1
