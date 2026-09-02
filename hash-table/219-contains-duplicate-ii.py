"""
Problem Description:
Given an integer array nums and an integer k, determine
whether there are two distinct indices i and j such that
nums[i] == nums[j] and abs(i - j) <= k.

Approach:
- Maintain a hash map storing the most recent index at which
  each value was encountered.
- For every element:
  - If it has appeared before, compare the current index with
    its most recent index.
  - If the distance is at most k, return True.
  - Otherwise, update the value's stored index to the current
    index.
- If no valid pair is found, return False.

Time Complexity:
O(n)

Reason:
- Each element is processed once.
- Hash-map lookup and update take O(1) average time.

Space Complexity:
O(n)

Reason:
- In the worst case, all elements are distinct and the map
  stores n values.
"""

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mapping = {}

        for  i in range(len(nums)):
            if nums[i] in mapping and abs(mapping[nums[i]] - i)<=k:
                    return True
            else:
                mapping[nums[i]] = i

        return False
