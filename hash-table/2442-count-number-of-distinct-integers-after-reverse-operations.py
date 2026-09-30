"""
Problem Description:
Given an array of positive integers, reverse the digits of every original
integer and append the reversed values to the array. Return the number of
distinct integers in the final array.

Approach:
- Create a helper function to reverse the digits of an integer.
- Iterate only over the original elements of nums.
- For each original number, add both the original number and its reversed
  value to a set.
- Since a set stores only unique values, its final size is the number of
  distinct integers in the resulting array.

Time Complexity:
O(n * d)

Reason:
- There are n original integers.
- Reversing an integer takes O(d), where d is its number of digits.
- Inserting into a set takes O(1) average time.
- Therefore the total complexity is O(n * d).

Space Complexity:
O(n)

Reason:
- The set can contain up to 2n distinct integers.
"""

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        
        def rev(n):
            new = 0
            while n:
                new=new*10+n%10
                n//=10
            return new

        size = len(nums)

        visited = set()
        for i in range(size):
            temp= rev(nums[i])
            visited.add(temp)
            visited.add(nums[i])

        return len(visited)

