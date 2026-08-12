"""
Problem Description:
Given an integer array nums and an integer k, find the
length of the longest contiguous subarray in which every
element occurs at most k times.

Approach:
- Maintain a sliding window using left and right pointers.
- Store the frequency of each element in the current window.
- Expand the window using right while the frequency of the
  current element is less than k.
- If the current element already occurs k times, move left
  and decrease the frequency of the element leaving the
  window.
- Track the maximum valid window length.

Time Complexity:
O(n)

Reason:
- The right pointer moves forward at most n times.
- The left pointer also moves forward at most n times.
- Although right may remain fixed for some iterations,
  each such iteration moves left forward.
- Therefore, the total number of pointer movements is O(n).

Space Complexity:
O(n)

Reason:
- The frequency dictionary can contain up to n distinct
  elements.
"""
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        freq = {

        }

        left =0
        right = 0

        maxArray = left-right 

        while right<len(nums):

            if nums[right] not in freq:
                freq[nums[right]] = 1
                right +=1
            elif freq[nums[right]]<k:
                freq[nums[right]]+=1
                right +=1

            elif freq[nums[right]] == k:
                freq[nums[left]]-=1
                left+=1
            maxArray = max(maxArray, right-left)
        return maxArray
                

