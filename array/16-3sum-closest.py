"""
Problem Description:
Given an integer array and a target, find three elements at distinct
indices whose sum is closest to the target. Return that sum.

Approach:
- Sort the array to enable the two-pointer technique.
- Fix one element nums[x].
- Convert the problem into finding two elements whose sum is closest
  to target - nums[x].
- Use left and right pointers to search for the closest pair.
- If the current pair sum is greater than the required target, move
  the right pointer left.
- If it is smaller, move the left pointer right.
- If it exactly matches the target, return target immediately.
- Track the closest three-element sum encountered.

Time Complexity:
O(n^2)

Reason:
- Sorting takes O(n log n).
- For each fixed element, the two-pointer scan takes O(n).
- Therefore the total complexity is O(n^2).

Space Complexity:
O(1) auxiliary space.

Reason:
- Only a constant number of variables are used apart from the sorting
  implementation.
- The array is sorted in-place.
"""

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        

        nums.sort()
        closest = None
        for x in  range(len(nums)):
            
            left = x+1
            right = len(nums)-1

            new_target = target - nums[x]
            while left<right:
                s = nums[left]+nums[right]

                if s>new_target:
                    right-=1

                elif s<new_target:
                    left+=1

                else:
                    return target
                
                if closest is None or abs(s-new_target)<abs(target-closest):
                    
                    closest = s+nums[x]
                    

        return closest

