"""
Problem Description:
Given a sorted array, remove duplicates in-place such
that each unique element appears at most twice.
Return the number of valid elements after modification.

Approach:
- Use two pointers:
  - i → position to place the next valid element.
  - idx → traverses the array.
- Always keep the first two occurrences of every number.
- For each new element:
  - If it is different from nums[i-2], place it at index i.
  - Otherwise, skip it.
- Return i as the length of the modified array.

Time Complexity:
O(n)

Reason:
- n = length of nums.
- Each element is visited exactly once.
- Every assignment is performed at most once.

Space Complexity:
O(1)

Reason:
- Uses only two pointer variables.
- Modifies the array in-place.
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 1

        for idx in range(1, len(nums)):

            if i == 1 or nums[idx] !=nums[i-2]:
                nums[i] = nums[idx]
                i+=1
        
        return i

