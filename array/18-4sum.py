"""
Problem Description:
Given an integer array nums and a target, find all unique quadruplets
whose elements sum to the target. All four elements must come from
distinct indices.

Approach:
Use sorting, nested loops, and the two-pointer technique.

1. Sort the array to enable efficient two-pointer traversal and duplicate
   elimination.
2. Fix the first element using pointer a.
3. Skip duplicate values of a to avoid generating repeated quadruplets.
4. Fix the second element using pointer b.
5. Skip duplicate values of b.
6. Calculate the remaining target after selecting the first two elements.
7. Use two pointers, left and right, to find the remaining pair:
   - If their sum equals the remaining target, store the quadruplet.
   - Skip duplicate values at both pointers.
   - Move both pointers inward.
   - If the sum is greater than the remaining target, decrement right.
   - Otherwise, increment left.

Time Complexity: O(n^3)
Reason: Sorting takes O(n log n). The two nested loops take O(n^2),
and for each pair, the two-pointer traversal takes O(n).
Therefore, the overall complexity is O(n^3).

Space Complexity: O(n) auxiliary space in the worst case.
Reason: Python's in-place sorting may require O(n) temporary storage.
The algorithm otherwise uses O(1) auxiliary space, excluding the
output list.
"""

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        
        nums.sort()
        ans = []

        for a in range(len(nums)):

            if a>0 and nums[a]==nums[a-1]:
                continue

            for b in range(a+1, len(nums)):

                if b>a+1 and nums[b]==nums[b-1]:
                    continue

                left = b+1
                right = len(nums)-1

                new_target= target - nums[b]-nums[a]
                while left<right:

                    if (nums[left]+ nums[right]) == new_target:
                        ans.append([nums[a], nums[b], nums[left], nums[right]])

                        while left<right and nums[left]== nums[left+1]:
                            left+=1

                        while left<right and nums[right] == nums[right-1]:
                            right-=1
                            
                        left+=1
                        right-=1
                    
                    elif nums[left]+nums[right]>new_target:
                        right-=1
                        
                    else:
                        left+=1

        return ans  

                    
