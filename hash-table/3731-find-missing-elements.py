"""
Problem Description:
Given an array of unique integers representing an
incomplete consecutive range, return all missing
integers in sorted order.

Approach:
- Store all elements in a hash map for O(1) average
  lookup.
- Find the minimum and maximum elements.
- Traverse every integer between the minimum and maximum.
- If a number is not present in the hash map, add it to
  the result.

Time Complexity:
O(n + R)

Reason:
- Building the hash map takes O(n).
- Finding the minimum and maximum takes O(n).
- Traversing the range takes O(R), where
  R = max(nums) - min(nums).

Space Complexity:
O(n)

Reason:
- The hash map stores all n elements of the array.
"""

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []
        
        mapping = {i: 0 for i in nums}

        minElement = min(nums)
        maxElement = max(nums)

        for i in range(minElement+1, maxElement):
            if i not in mapping:
                result.append(i)

        return result
