"""
Problem Description:
Given an integer array nums, count the non-empty subarrays whose
distinct values, ordered by first appearance, occur exactly
1, 2, 3, ..., k times, respectively.

Approach:
- Fix each possible left endpoint of a subarray.
- Maintain a frequency dictionary while extending the right endpoint.
- Use checker(freq) to verify whether the frequencies match the
  required staircase sequence.
- Increment the answer whenever the current subarray is valid.
- Return the total count.

Time Complexity:
O(n^3)

Reason:
- There are O(n^2) possible subarrays.
- For each subarray, checker iterates through up to O(n) distinct
  values to verify their frequencies.
- Therefore, the total time complexity is O(n^3).

Space Complexity:
O(n)

Reason:
- The frequency dictionary can store up to n distinct values.
- The checker uses only a constant amount of additional space.
"""
class Solution:
    def countStaircase(self, nums: list[int]) -> int:

        def checker(freq):
            for i, count in enumerate(freq.values(), start=1):
                if count != i:
                    return False
            return True

        count=0
        for left in range(len(nums)):
            freq = {}
            for right in range(left, len(nums)):

                if nums[right] not in freq:
                    freq[nums[right]]=1

                else:
                    freq[nums[right]]+=1

                if checker(freq):
                    count+=1

        return count
